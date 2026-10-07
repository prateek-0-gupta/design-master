// Fix-up for sites whose content scrolls inside an inner container (fullPage shot = 1 viewport).
// For each page (home + subpages from site_meta.json): find the largest scrollable element, step it
// by its clientHeight, screenshot each step, and stitch with stitch.py into the same shots/*.png name.
const { launch, sleep } = require('./lib');
const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
const RAW = path.join(__dirname, '../raw/brandguidelines');
(async () => {
  const { browser, ctx } = await launch();
  for (const id of process.argv.slice(2)) {
    const d = path.join(RAW, id); const meta = JSON.parse(fs.readFileSync(path.join(d, 'site_meta.json')));
    const pages = [['d00_home', meta.requested], ...meta.subpages.filter(s => s.ok).map((s, i) => [`d0${i + 1}_sub`, s.href])];
    for (const [name, url] of pages) {
      const page = await ctx.newPage();
      try {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }); await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {}); await sleep(3500);
        for (const b of await page.getByRole('button', { name: /^(accept|accept all|allow all|agree|got it|reject all|reject|decline)$/i }).all()) await b.click({ timeout: 1500 }).catch(() => {});
        const info = await page.evaluate(() => {
          let best = null, bestH = 0;
          for (const el of document.querySelectorAll('body *')) { const s = getComputedStyle(el);
            if (/(auto|scroll)/.test(s.overflowY) && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > bestH) { best = el; bestH = el.scrollHeight; } }
          if (!best) return null; best.setAttribute('data-cap-scroller', '1'); const r = best.getBoundingClientRect();
          return { h: best.scrollHeight, ch: best.clientHeight, top: r.top };
        });
        if (!info) {
          // wheel mode (smooth-scroll libraries): viewport screenshots per wheel step until frames stop changing
          await page.mouse.move(900, 450); let prev = null, k = 0;
          for (const t of fs.readdirSync(path.join(d, 'tiles')).filter(t => t.startsWith(name + '_'))) fs.unlinkSync(path.join(d, 'tiles', t));
          for (; k < 30; k++) {
            const buf = await page.screenshot({ type: 'jpeg', quality: 85 });
            if (prev && buf.equals(prev)) break;
            fs.writeFileSync(path.join(d, 'tiles', `${name}_w${String(k + 1).padStart(2, '0')}.jpg`), buf); prev = buf;
            await page.mouse.wheel(0, 800); await sleep(1400);
          }
          console.log('wheel', id, name, k, 'frames'); await page.close(); continue;
        }
        const steps = Math.min(Math.ceil(info.h / info.ch), 30); const parts = [];
        for (let k = 0; k < steps; k++) {
          await page.evaluate(([k]) => { const el = document.querySelector('[data-cap-scroller]'); el.scrollTop = k * el.clientHeight; }, [k]); await sleep(900);
          const actual = await page.evaluate(() => document.querySelector('[data-cap-scroller]').scrollTop);
          const f = path.join(d, 'shots', `_${name}_part${String(k).padStart(2, '0')}_${actual}.png`); await page.screenshot({ path: f }); parts.push(f);
        }
        execFileSync('python3', ['-I', path.join(__dirname, 'stitch.py'), path.join(d, 'shots', `${name}.png`), String(Math.round(info.top)), String(info.ch), ...parts]);
        parts.forEach(f => fs.unlinkSync(f));
        // drop stale tiles so tile_shots.py regenerates
        for (const t of fs.readdirSync(path.join(d, 'tiles')).filter(t => t.startsWith(name + '_'))) fs.unlinkSync(path.join(d, 'tiles', t));
        console.log('stitched', id, name, steps, 'steps', info.h, 'px');
      } catch (e) { console.log('FAIL', id, name, e.message.slice(0, 120)); }
      await page.close();
    }
  }
  await browser.close();
})();
