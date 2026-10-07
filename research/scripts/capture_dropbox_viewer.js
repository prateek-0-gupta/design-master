// Fallback for Dropbox PDFs with downloads disabled: screenshot each page from the in-browser viewer.
// Usage: node capture_dropbox_viewer.js <id> <dropbox-url>  -> raw/brandguidelines/{id}/pages/pNNN.jpg
const { launch, sleep } = require('./lib'); const fs = require('fs'); const path = require('path');
(async () => {
  const [id, url] = process.argv.slice(2); const out = path.join(__dirname, '../raw/brandguidelines', id, 'pages'); fs.mkdirSync(out, { recursive: true });
  const { browser, ctx } = await launch({ viewport: { width: 1600, height: 1200 } }); const p = await ctx.newPage();
  await p.goto(url, { timeout: 60000 }); await sleep(7000);
  await p.getByRole('button', { name: 'Decline' }).click({ timeout: 3000 }).catch(() => {});
  await p.getByRole('button', { name: /close/i }).first().click({ timeout: 2000 }).catch(() => {});
  const total = parseInt((await p.evaluate(() => document.body.innerText.match(/Page \d+ of (\d+)\b/)?.[1])) || '0');
  const seen = new Set();
  for (let step = 0; step < total * 4 && seen.size < total; step++) {
    const pages = await p.$$('div[class*="_page_"]');
    for (const el of pages) {
      const info = await el.evaluate(e => { const r = e.getBoundingClientRect(); const img = e.querySelector('img'); let sc = e.parentElement; while (sc && !(sc.scrollHeight > sc.clientHeight + 100 && /(auto|scroll)/.test(getComputedStyle(sc).overflowY))) sc = sc.parentElement; return { top: r.top, bottom: r.bottom, h: r.height, off: Math.round(r.top + (sc ? sc.scrollTop : scrollY)), src: img ? img.src : '', ok: !!(img && img.complete && img.naturalWidth > 0) }; });
      if (!info.ok) continue;
      const idx = Math.round(info.off / (info.h + 16)) + 1;   // approximate; corrected below by unique sort
      const key = info.src; if (seen.has(key)) continue; seen.add(key);
      await el.screenshot({ path: path.join(out, `_off${String(info.off + 1000000).padStart(8, '0')}.jpg`), type: 'jpeg', quality: 88 });
    }
    const moved = await p.evaluate(() => { let best = null; for (const el of document.querySelectorAll('*')) { const s = getComputedStyle(el); if (/(auto|scroll)/.test(s.overflowY) && el.scrollHeight > el.clientHeight + 100 && (!best || el.scrollHeight > best.scrollHeight)) best = el; }
      if (!best) return -1; const before = best.scrollTop; best.scrollTop += Math.round(best.clientHeight * 0.45); return best.scrollTop - before; });
    if (moved === 0 && step > 2) break;
    await sleep(1200);
  }
  // rename by offset order -> p001..
  const files = fs.readdirSync(out).filter(f => f.startsWith('_off')).sort();
  files.forEach((f, i) => fs.renameSync(path.join(out, f), path.join(out, `p${String(i + 1).padStart(3, '0')}.jpg`)));
  console.log(id, 'captured', files.length, 'of', total); await browser.close();
})();
