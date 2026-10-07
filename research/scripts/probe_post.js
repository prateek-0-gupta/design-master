const { launch, gotoPast } = require('./lib');
const fs = require('fs');
(async () => {
  const { browser, ctx } = await launch(); const page = await ctx.newPage();
  console.log(await gotoPast(page, 'https://www.inspora.design/posts/' + process.argv[2]));
  const html = await page.content(); fs.writeFileSync('/tmp/claude-0/-home-user-design-master/5e2f0773-34d4-5ce4-820e-cbbc2ddb4914/scratchpad/post.html', html);
  await page.screenshot({ path: '/tmp/claude-0/-home-user-design-master/5e2f0773-34d4-5ce4-820e-cbbc2ddb4914/scratchpad/post.png' });
  console.log(await page.title());
  await browser.close();
})();
