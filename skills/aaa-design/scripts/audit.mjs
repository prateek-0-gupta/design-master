#!/usr/bin/env node
// aaa-design audit: render a page, screenshot it at 3 widths, and check the hard gates.
//
//   node audit.mjs <file.html | http(s)://url> [outDir=./audit]
//
// Output: outDir/shot-390.png, shot-768.png, shot-1440.png (+ shot-1440-reduced.png) and report.json / report.md.
// Exit code 1 if any HARD gate fails. Read the screenshots yourself afterwards; this script only measures.
//
// Hard gates:   text contrast (AA), horizontal overflow at 390px, visible keyboard focus,
//               reduced-motion respected, min text size 12px, images have alt, controls have names.
// Warnings:     touch targets < 44px on mobile, heading structure, >3 font families, >4 radii, >1 accent hue.
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const require = createRequire(import.meta.url);
function loadPlaywright() {
  const tries = ['playwright', 'playwright-core', '/opt/node-tools/node_modules/playwright', '/usr/local/lib/node_modules/playwright', '/opt/node22/lib/node_modules/playwright'];
  for (const t of tries) { try { return require(t); } catch {} }
  console.error('Playwright not found. Install it (npm i -D playwright) or set NODE_PATH.'); process.exit(2);
}
const { chromium } = loadPlaywright();
const exe = process.env.CHROMIUM_PATH || (fs.existsSync('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') ? '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' : undefined);

const target = process.argv[2];
if (!target) { console.error('usage: node audit.mjs <file.html|url> [outDir]'); process.exit(2); }
const outDir = path.resolve(process.argv[3] || 'audit');
fs.mkdirSync(outDir, { recursive: true });
const url = /^https?:/.test(target) ? target : pathToFileURL(path.resolve(target)).href;

// ---- in-page measurement (runs in the browser) ----
function measure() {
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  const L = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const over = (top, bot) => ({ r: top.r * top.a + bot.r * (1 - top.a), g: top.g * top.a + bot.g * (1 - top.a), b: top.b * top.a + bot.b * (1 - top.a), a: 1 });
  const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  function background(el) {
    const layers = []; let imageBehind = false;
    for (let e = el; e; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.backgroundImage && s.backgroundImage !== 'none') imageBehind = true;
      const c = parse(s.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
    }
    let bg = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = layers.length - 1; i >= 0; i--) bg = over(layers[i], bg);
    return { bg, imageBehind };
  }
  const fails = [], seen = new Set(); let textNodes = 0, tiny = [];
  for (const el of document.querySelectorAll('body *')) {
    if (!el.checkVisibility || !el.checkVisibility({ opacityProperty: true, visibilityProperty: true })) continue;
    const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim().length > 0);
    if (!own.length) continue;
    const s = getComputedStyle(el); const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
    if (el.closest('[aria-hidden="true"]')) continue;
    textNodes++;
    const size = parseFloat(s.fontSize), weight = parseInt(s.fontWeight) || 400;
    if (size < 12) tiny.push({ text: el.textContent.trim().slice(0, 40), size });
    let fg = parse(s.color); if (!fg) continue;
    // include element opacity chain
    let op = 1; for (let e = el; e; e = e.parentElement) op *= parseFloat(getComputedStyle(e).opacity);
    const { bg, imageBehind } = background(el);
    fg = over({ ...fg, a: fg.a * op }, bg);
    const l1 = L(fg), l2 = L(bg); const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const need = large ? 3 : 4.5;
    if (ratio < need) {
      const key = hex(fg) + hex(bg) + size;
      if (!seen.has(key)) { seen.add(key); fails.push({ text: el.textContent.trim().slice(0, 50), fg: hex(fg), bg: hex(bg), ratio: +ratio.toFixed(2), need, size, imageBehind, selector: el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '') }); }
    }
  }
  // inventory
  const fams = new Set(), radii = new Set(), sat = new Set();
  for (const el of document.querySelectorAll('body *')) {
    const s = getComputedStyle(el);
    fams.add(s.fontFamily.split(',')[0].replace(/["']/g, '').trim());
    if (s.borderTopLeftRadius !== '0px' && !s.borderTopLeftRadius.includes('%')) radii.add(Math.min(parseFloat(s.borderTopLeftRadius), 999));
    for (const c of [s.backgroundColor, s.color]) { const p = parse(c); if (!p || p.a < 0.5) continue; const mx = Math.max(p.r, p.g, p.b), mn = Math.min(p.r, p.g, p.b); if (mx - mn > 60) sat.add(Math.round(Math.atan2(Math.sqrt(3) * (p.g - p.b), 2 * p.r - p.g - p.b) * 180 / Math.PI / 30)); }
  }
  const imgs = [...document.querySelectorAll('img')].filter(i => !i.hasAttribute('alt')).length;
  const unnamed = [...document.querySelectorAll('button, a[href], input, select, textarea, [role=button]')].filter(e => {
    const name = (e.getAttribute('aria-label') || e.getAttribute('title') || e.textContent || e.getAttribute('placeholder') || e.value || '').trim();
    const labelled = e.id && document.querySelector(`label[for="${e.id}"]`); return !name && !labelled && !e.getAttribute('aria-labelledby') && !e.querySelector('img[alt]:not([alt=""])');
  }).map(e => e.outerHTML.slice(0, 80));
  const h = [...document.querySelectorAll('h1,h2,h3,h4')].map(x => +x.tagName[1]);
  let skips = 0; for (let i = 1; i < h.length; i++) if (h[i] - h[i - 1] > 1) skips++;
  return { textNodes, contrastFails: fails.sort((a, b) => a.ratio - b.ratio), tiny: tiny.slice(0, 10), fontFamilies: [...fams].filter(Boolean), radii: [...radii].sort((a, b) => a - b), accentHueBuckets: sat.size, imgsWithoutAlt: imgs, unnamedControls: unnamed.slice(0, 10), h1: h.filter(x => x === 1).length, headingSkips: skips,
    reducedMotionCSS: [...document.styleSheets].some(sh => { try { return [...sh.cssRules].some(r => r.media && /prefers-reduced-motion/.test(r.media.mediaText)); } catch { return false; } }) };
}

function targets() {
  const small = [];
  for (const e of document.querySelectorAll('button, a[href], input, select, textarea, [role=button], [role=tab], [role=switch], summary')) {
    const r = e.getBoundingClientRect(); if (!r.width || !r.height) continue;
    const inText = e.tagName === 'A' && e.closest('p, li') && getComputedStyle(e).display === 'inline';
    if (!inText && (r.width < 44 || r.height < 44)) small.push({ el: e.outerHTML.slice(0, 70), w: Math.round(r.width), h: Math.round(r.height) });
  }
  return small;
}

(async () => {
  const browser = await chromium.launch({ executablePath: exe });
  const report = { url, widths: {}, gates: {}, warnings: [] };
  for (const w of [390, 768, 1440]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: w === 390 ? 844 : 900 }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => {});
    await page.waitForTimeout(800);
    // scroll through the page so scroll-triggered reveals (IntersectionObserver) fire, then return to top
    await page.evaluate(async () => { const h = document.documentElement.scrollHeight; for (let y = 0; y < h + innerHeight; y += Math.max(300, innerHeight * 0.5)) { scrollTo(0, y); await new Promise(r => setTimeout(r, 350)); } scrollTo(0, 0); await new Promise(r => setTimeout(r, 1500)); });
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await page.screenshot({ path: path.join(outDir, `shot-${w}.png`), fullPage: true });
    report.widths[w] = { overflowPx: overflow };
    if (w === 390) report.widths[w].smallTargets = await page.evaluate(targets);
    if (w === 1440) {
      Object.assign(report, await page.evaluate(measure));
      // keyboard focus visibility: tab through up to 12 stops, compare styles before/after focus
      const stops = [];
      for (let i = 0; i < 12; i++) {
        await page.keyboard.press('Tab');
        const info = await page.evaluate(() => {
          const e = document.activeElement; if (!e || e === document.body) return null;
          const s = getComputedStyle(e);
          const visible = (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) || (s.boxShadow && s.boxShadow !== 'none');
          return { el: e.tagName.toLowerCase() + (e.textContent ? ':' + e.textContent.trim().slice(0, 20) : ''), visible };
        });
        if (info) stops.push(info);
      }
      report.focusStops = stops;
    }
    await ctx.close();
  }
  // reduced motion: count running animations with and without the preference
  const anim = async reduce => { const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: reduce ? 'reduce' : 'no-preference' }); const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => {}); await p.waitForTimeout(1500);
    const n = await p.evaluate(() => document.getAnimations().filter(a => a.playState === 'running' && (a.effect?.getTiming?.().duration || 0) > 200).length);
    if (reduce) await p.screenshot({ path: path.join(outDir, 'shot-1440-reduced.png') }); await ctx.close(); return n; };
  report.runningAnimations = { normal: await anim(false), reduced: await anim(true) };
  await browser.close();

  // ---- gates ----
  const g = report.gates;
  g.contrast = { pass: report.contrastFails.filter(f => !f.imageBehind).length === 0, fails: report.contrastFails.length, note: 'text over background-images is listed but must be verified visually' };
  g.noOverflow390 = { pass: report.widths[390].overflowPx <= 1, overflowPx: report.widths[390].overflowPx };
  g.focusVisible = { pass: report.focusStops.length === 0 ? null : report.focusStops.every(s => s.visible), stops: report.focusStops.length, invisible: report.focusStops.filter(s => !s.visible).map(s => s.el) };
  g.reducedMotion = { pass: report.runningAnimations.normal === 0 || report.runningAnimations.reduced < report.runningAnimations.normal || report.runningAnimations.reduced === 0, ...report.runningAnimations, hasMediaQuery: report.reducedMotionCSS };
  g.minTextSize = { pass: report.tiny.length === 0, tiny: report.tiny };
  g.altAndNames = { pass: report.imgsWithoutAlt === 0 && report.unnamedControls.length === 0, imgsWithoutAlt: report.imgsWithoutAlt, unnamedControls: report.unnamedControls };
  const w = report.warnings;
  if (report.widths[390].smallTargets.length) w.push(`${report.widths[390].smallTargets.length} touch targets < 44px at 390px`);
  if (report.h1 !== 1) w.push(`page has ${report.h1} <h1> (expected 1)`);
  if (report.headingSkips) w.push(`${report.headingSkips} heading level skips`);
  if (report.fontFamilies.length > 3) w.push(`${report.fontFamilies.length} font families: ${report.fontFamilies.join(', ')}`);
  if (report.radii.length > 4) w.push(`${report.radii.length} distinct radii: ${report.radii.join(', ')} (aim for 2-3 + pill)`);
  if (report.accentHueBuckets > 2) w.push(`${report.accentHueBuckets} saturated hue families (aim for 1 accent unless colour-coding categories)`);
  if (!report.reducedMotionCSS) w.push('no @media (prefers-reduced-motion) rule found');
  const hard = Object.entries(g).filter(([, v]) => v.pass === false).map(([k]) => k);
  report.hardFails = hard;
  fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 1));
  const md = [`# Audit: ${url}`, '', `**Hard gates:** ${hard.length ? 'FAIL → ' + hard.join(', ') : 'all pass'}`, '',
    ...Object.entries(g).map(([k, v]) => `- ${v.pass === false ? '✗' : v.pass === null ? '?' : '✓'} ${k}: ${JSON.stringify(Object.fromEntries(Object.entries(v).filter(([kk]) => kk !== 'pass'))).slice(0, 300)}`),
    '', '**Warnings:**', ...(w.length ? w.map(x => '- ' + x) : ['- none']), '',
    '**Worst contrast pairs:**', ...report.contrastFails.slice(0, 12).map(f => `- ${f.ratio}:1 (needs ${f.need}) ${f.fg} on ${f.bg} ${f.size}px "${f.text}" <${f.selector}>${f.imageBehind ? ' [over image]' : ''}`),
    '', `Fonts: ${report.fontFamilies.join(', ')} | radii: ${report.radii.join(', ')}`, '', `Screenshots: ${['shot-390.png', 'shot-768.png', 'shot-1440.png', 'shot-1440-reduced.png'].map(f => path.join(outDir, f)).join(', ')}`];
  fs.writeFileSync(path.join(outDir, 'report.md'), md.join('\n'));
  console.log(md.join('\n'));
  process.exit(hard.length ? 1 : 0);
})();
