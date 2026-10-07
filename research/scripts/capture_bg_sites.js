// Phase 2: capture live brand-guideline sites, hosted brand platforms, templates and promoted pages.
// Per entry (raw/brandguidelines/{id}/): desktop 1440 + mobile 390 full-page screenshots (tiled later by
// tile_shots.py), up to 6 brand-relevant subpages at 1440, every CSS file served, and an in-page
// computed-style census (census_*.json) of fonts, sizes, colours, radii, shadows and transitions.
const { launch, sleep } = require('./lib');
const fs = require('fs'); const path = require('path');
const RAW = path.join(__dirname, '../raw/brandguidelines');
const inv = JSON.parse(fs.readFileSync(path.join(__dirname, '../inventory.json')))
  .filter(r => r.source === 'brandguidelines' && r.asset_type !== 'pdf');
const only = process.argv.slice(2);
const MAX_H = 26000;
const KEY = /logo|colou?r|typo|type|font|image|photo|icon|motion|anim|voice|tone|illustr|layout|grid|component|brand|identity|visual|guideline|principle|foundation|spacing|elevation|graphic|pattern|accessib/i;

async function dismiss(page) {
  for (const re of [/^(accept|accept all|allow all|agree|i agree|got it|ok|okay|reject all|reject|decline|only necessary|necessary only|continue)$/i]) {
    for (const b of await page.getByRole('button', { name: re }).all().catch(() => [])) { await b.click({ timeout: 1500 }).catch(() => {}); }
  }
  await page.evaluate(() => { for (const el of document.querySelectorAll('[id*=onetrust],[class*=cookie],[id*=cookie],[class*=consent],[id*=consent]')) { const s = getComputedStyle(el); if (s.position === 'fixed' || s.position === 'sticky') el.remove(); } }).catch(() => {});
}
async function scrollAll(page) {
  await page.evaluate(async (MAX_H) => {
    const step = 700; let y = 0;
    while (y < Math.min(document.documentElement.scrollHeight, MAX_H)) { window.scrollTo(0, y); y += step; await new Promise(r => setTimeout(r, 180)); }
    window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 600));
  }, MAX_H).catch(() => {});
}
function census() {
  const tally = (m, k) => { if (k == null || k === '') return; m[k] = (m[k] || 0) + 1; };
  const R = { fontFamily: {}, fontSize: {}, fontWeight: {}, lineHeight: {}, letterSpacing: {}, textColor: {}, bg: {}, radius: {}, shadow: {}, transition: {}, border: {}, textTransform: {}, typePairs: {} };
  const els = [...document.querySelectorAll('body *')].slice(0, 12000);
  for (const el of els) {
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none') continue;
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (hasText) {
      tally(R.fontFamily, s.fontFamily); tally(R.fontSize, s.fontSize); tally(R.fontWeight, s.fontWeight); tally(R.lineHeight, s.lineHeight);
      tally(R.letterSpacing, s.letterSpacing); tally(R.textColor, s.color); tally(R.textTransform, s.textTransform);
      tally(R.typePairs, `${s.fontFamily.split(',')[0].replace(/"/g, '')} | ${s.fontSize} | ${s.fontWeight} | lh ${s.lineHeight} | ls ${s.letterSpacing}`);
    }
    if (s.backgroundColor !== 'rgba(0, 0, 0, 0)') tally(R.bg, s.backgroundColor);
    if (s.borderRadius !== '0px') tally(R.radius, s.borderRadius);
    if (s.boxShadow !== 'none') tally(R.shadow, s.boxShadow);
    if (s.transitionDuration !== '0s') tally(R.transition, `${s.transitionProperty} ${s.transitionDuration} ${s.transitionTimingFunction}`);
    if (s.borderTopStyle !== 'none' && s.borderTopWidth !== '0px') tally(R.border, `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`);
  }
  const vars = {}; const cs = getComputedStyle(document.documentElement);
  for (let i = 0; i < cs.length; i++) { const p = cs[i]; if (p.startsWith('--')) vars[p] = cs.getPropertyValue(p).trim().slice(0, 200); }
  for (const sh of document.styleSheets) { try { for (const rule of sh.cssRules) { if (rule.selectorText && /(:root|^html|^body)/.test(rule.selectorText)) for (const p of rule.style) if (p.startsWith('--') && !(p in vars)) vars[p] = rule.style.getPropertyValue(p).trim().slice(0, 200); } } catch (e) {} }
  const fonts = [...document.fonts].filter(f => f.status === 'loaded').map(f => `${f.family} ${f.weight} ${f.style}`);
  const sort = o => Object.fromEntries(Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, 40));
  const out = {}; for (const k in R) out[k] = sort(R[k]);
  return { url: location.href, title: document.title, scrollHeight: document.documentElement.scrollHeight, customProperties: vars, loadedFonts: [...new Set(fonts)], ...out,
    headings: [...document.querySelectorAll('h1,h2,h3')].slice(0, 80).map(h => `${h.tagName} ${h.innerText.trim().slice(0, 80)}`),
    nav: [...document.querySelectorAll('a[href]')].map(a => ({ t: a.innerText.trim().slice(0, 60), h: a.href })).filter(x => x.t) };
}
async function shoot(page, file) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight).catch(() => 900);
  const w = page.viewportSize().width;
  if (h <= MAX_H) await page.screenshot({ path: file, fullPage: true, timeout: 120000 });
  else await page.screenshot({ path: file, fullPage: true, clip: { x: 0, y: 0, width: w, height: MAX_H }, timeout: 120000 });
  return h;
}
async function visit(page, url, waitMs = 3500) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {});
  for (let i = 0; i < 20 && /just a moment|security|checkpoint|attention required/i.test(await page.title().catch(() => '')); i++) await sleep(2000);
  await page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {});
  await sleep(waitMs); await dismiss(page); await scrollAll(page); await sleep(800);
}
(async () => {
  const { browser, ctx } = await launch();
  const mob = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
  const fails = {};
  for (const r of inv) {
    if (only.length && !only.includes(r.id)) continue;
    const d = path.join(RAW, r.id); fs.mkdirSync(path.join(d, 'shots'), { recursive: true });
    if (fs.existsSync(path.join(d, '_site_done')) && !only.length) continue;
    const css = []; const page = await ctx.newPage();
    page.on('response', async res => { if ((res.headers()['content-type'] || '').includes('text/css')) { try { css.push(`/* ${res.url()} */\n` + await res.text()); } catch {} } });
    try {
      const wait = r.asset_type === 'figma-prototype' ? 15000 : 3500;
      await visit(page, r.url, wait);
      const h = await shoot(page, path.join(d, 'shots', 'd00_home.png'));
      const c = await page.evaluate(census); c.fullHeight = h;
      fs.writeFileSync(path.join(d, 'census_home.json'), JSON.stringify(c, null, 1));
      // subpages: same host, brand-relevant keyword in link text or path
      const base = new URL(page.url());
      const cands = [];
      for (const l of c.nav) {
        try { const u = new URL(l.h); u.hash = '';
          if (u.host !== base.host || u.href === base.href || /\.(pdf|zip|png|jpg|svg)$/i.test(u.pathname)) continue;
          if (!(KEY.test(l.t) || KEY.test(u.pathname))) continue;
          if (r.asset_type === 'template-page' || r.asset_type === 'promoted-site') continue;
          if (!cands.find(x => x.href === u.href)) cands.push({ href: u.href, t: l.t });
        } catch {}
      }
      const subs = cands.slice(0, 6); const subLog = [];
      for (const [i, s] of subs.entries()) {
        try { await visit(page, s.href, 2500); const sh = await shoot(page, path.join(d, 'shots', `d0${i + 1}_sub.png`));
          const sc = await page.evaluate(census); sc.fullHeight = sh; fs.writeFileSync(path.join(d, `census_sub${i + 1}.json`), JSON.stringify(sc, null, 1)); subLog.push({ ...s, ok: true });
        } catch (e) { subLog.push({ ...s, ok: false, err: e.message.slice(0, 120) }); }
      }
      // mobile home
      const mp = await mob.newPage();
      try { await visit(mp, r.url, wait); await shoot(mp, path.join(d, 'shots', 'm00_home.png')); } catch (e) { subLog.push({ mobile: false, err: e.message.slice(0, 120) }); }
      await mp.close();
      fs.writeFileSync(path.join(d, 'all.css'), css.join('\n\n'));
      fs.writeFileSync(path.join(d, 'site_meta.json'), JSON.stringify({ requested: r.url, final: page.url(), title: c.title, subpages: subLog, cssFiles: css.length }, null, 1));
      fs.writeFileSync(path.join(d, '_site_done'), 'ok');
      console.log('ok', r.id, 'subs', subs.length, 'h', h);
    } catch (e) { fails[r.id] = e.message.slice(0, 300); console.log('FAIL', r.id, e.message.slice(0, 150)); }
    await page.close();
  }
  fs.writeFileSync(path.join(RAW, `_site_failures${only.length ? '_partial' : ''}.json`), JSON.stringify(fails, null, 1));
  await browser.close();
})();
