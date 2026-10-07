// Figma prototype whose frame scrolls vertically: wheel-step over the canvas, screenshot until static.
// Usage: node capture_figma_scroll.js <id> <url> [maxSteps]  -> tiles/figscroll_NN.jpg
const { launch, sleep } = require('./lib'); const fs = require('fs'); const path = require('path');
(async () => {
  const [id, url, max = '80'] = process.argv.slice(2); const d = path.join(__dirname, '../raw/brandguidelines', id, 'tiles'); fs.mkdirSync(d, { recursive: true });
  const { browser, ctx } = await launch(); const p = await ctx.newPage();
  await p.goto(url, { timeout: 90000 }); await sleep(20000); await p.mouse.move(720, 600);
  let prev = null, n = 0, same = 0;
  for (let k = 0; k < +max; k++) {
    const buf = await p.screenshot({ type: 'jpeg', quality: 88 });
    if (prev && buf.equals(prev)) { if (++same >= 3) break; } else { same = 0; fs.writeFileSync(path.join(d, `figscroll_${String(++n).padStart(2, '0')}.jpg`), buf); }
    prev = buf; await p.mouse.wheel(0, 600); await sleep(1500);
  }
  console.log(id, 'frames', n); await browser.close();
})();
