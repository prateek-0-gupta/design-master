// Figma prototypes render to <canvas>; step through frames with the viewer's "Next frame" button.
// Usage: node capture_figma_proto.js <id> <url> [maxFrames]  -> tiles/figma_fNN.jpg
const { launch, sleep } = require('./lib'); const fs = require('fs'); const path = require('path');
(async () => {
  const [id, url, max = '60'] = process.argv.slice(2); const d = path.join(__dirname, '../raw/brandguidelines', id, 'tiles'); fs.mkdirSync(d, { recursive: true });
  const { browser, ctx } = await launch(); const p = await ctx.newPage();
  await p.goto(url, { timeout: 90000 }); await sleep(20000);
  let prev = null, n = 0, same = 0;
  for (let k = 0; k < +max; k++) {
    const buf = await p.screenshot({ type: 'jpeg', quality: 88 });
    if (prev && buf.equals(prev)) { if (++same >= 2) break; } else { same = 0; fs.writeFileSync(path.join(d, `figma_f${String(++n).padStart(2, '0')}.jpg`), buf); }
    prev = buf;
    await p.getByRole('button', { name: 'Next frame' }).click({ timeout: 5000, force: true }).catch(() => p.keyboard.press('ArrowRight'));
    await sleep(3500);
  }
  console.log(id, 'frames', n); await browser.close();
})();
