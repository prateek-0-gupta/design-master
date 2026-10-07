// Phase 2a: for every Inspora post, save the rendered post page (HTML + 1440x900 screenshot)
// and the full post object (post.json) parsed from the RSC payload. Resumable.
const { launch, gotoPast, sleep } = require('./lib');
const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
const RAW = path.join(__dirname, '../raw/inspora');
const inv = JSON.parse(fs.readFileSync(path.join(__dirname, '../inventory.json'))).filter(r => r.source === 'inspora');
(async () => {
  let { browser, ctx } = await launch(); let page = await ctx.newPage();
  const fails = [];
  for (const [i, r] of inv.entries()) {
    const slug = r.id.replace(/^insp-/, ''); const dir = path.join(RAW, slug);
    if (fs.existsSync(path.join(dir, 'post.json'))) continue;
    fs.mkdirSync(dir, { recursive: true });
    let ok = false;
    for (let a = 0; a < 3 && !ok; a++) {
      try {
        const passed = await gotoPast(page, r.url);
        if (!passed) throw new Error('challenge not passed');
        await sleep(2500);
        const html = await page.content();
        fs.writeFileSync(path.join(dir, 'page.html'), html);
        const post = execFileSync('python3', ['-I', path.join(__dirname, 'rsc_post.py'), path.join(dir, 'page.html')]).toString();
        if (post.trim() === 'null') throw new Error('no post object in RSC');
        await page.screenshot({ path: path.join(dir, 'page.png') });
        fs.writeFileSync(path.join(dir, 'post.json'), post);
        ok = true;
      } catch (e) {
        console.log('retry', slug, a, e.message.slice(0, 100)); await sleep(8000 * (a + 1));
        if (a === 1) { await browser.close(); ({ browser, ctx } = await launch()); page = await ctx.newPage(); }
      }
    }
    if (!ok) fails.push(slug);
    if (i % 20 === 0) console.log(i, slug);
    await sleep(800);
  }
  fs.writeFileSync(path.join(RAW, '_page_failures.json'), JSON.stringify(fails));
  console.log('done, failures', fails.length);
  await browser.close();
})();
