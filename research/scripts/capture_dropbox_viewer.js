// Fallback for Dropbox PDFs with downloads disabled: screenshot each page from the in-browser viewer.
// Usage: node capture_dropbox_viewer.js <id> <dropbox-url>  -> raw/brandguidelines/{id}/pages/pNNN.jpg
const { launch, sleep } = require('./lib'); const fs = require('fs'); const path = require('path');
(async () => {
  const [id, url] = process.argv.slice(2); const out = path.join(__dirname, '../raw/brandguidelines', id, 'pages'); fs.mkdirSync(out, { recursive: true });
  const { browser, ctx } = await launch({ viewport: { width: 1600, height: 1200 } }); const p = await ctx.newPage();
  await p.goto(url, { timeout: 60000 }); await sleep(7000);
  await p.getByRole('button', { name: 'Decline' }).click({ timeout: 3000 }).catch(() => {});
  await p.getByRole('button', { name: /close/i }).first().click({ timeout: 2000 }).catch(() => {});
  const total = parseInt((await p.evaluate(() => document.body.innerText.match(/Page \d+ of (\d+)/)?.[1])) || '0');
  const seen = new Set();
  for (let step = 0; step < total * 4 && seen.size < total; step++) {
    const pages = await p.$$('div[class*="_page_"]');
    for (const el of pages) {
      const info = await el.evaluate(e => { const r = e.getBoundingClientRect(); const img = e.querySelector('img'); return { top: r.top, bottom: r.bottom, h: r.height, off: e.offsetTop, ok: !!(img && img.complete && img.naturalWidth > 0) }; });
      if (!info.ok || info.top < 0 || info.bottom > 1200) continue;
      const idx = Math.round(info.off / (info.h + 16)) + 1;   // approximate; corrected below by unique sort
      const key = info.off; if (seen.has(key)) continue; seen.add(key);
      await el.screenshot({ path: path.join(out, `_off${String(key).padStart(7, '0')}.jpg`), type: 'jpeg', quality: 88 });
    }
    await p.mouse.move(600, 700); await p.mouse.wheel(0, 500); await sleep(900);
  }
  // rename by offset order -> p001..
  const files = fs.readdirSync(out).filter(f => f.startsWith('_off')).sort();
  files.forEach((f, i) => fs.renameSync(path.join(out, f), path.join(out, `p${String(i + 1).padStart(3, '0')}.jpg`)));
  console.log(id, 'captured', files.length, 'of', total); await browser.close();
})();
