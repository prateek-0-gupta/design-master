// Enumerate brandguidelines.net/templates (+ load more), and re-verify homepage with slow Load More.
const { launch, sleep } = require('./lib');
const fs = require('fs');
const OUT = __dirname + '/../raw/brandguidelines/_enum';
async function exhaust(page) {
  let clicks = 0;
  for (let i = 0; i < 80; i++) {
    for (let y = 0; y < 30; y++) { await page.mouse.wheel(0, 1500); await sleep(100); }
    await sleep(2500);
    const btn = page.getByText(/^Load More$/i).first();
    if (!(await btn.count()) || !(await btn.isVisible().catch(() => false))) break;
    await btn.scrollIntoViewIfNeeded(); await btn.click(); clicks++; await sleep(4000);
  }
  return clicks;
}
const extract = page => page.$$eval('a[href]', as => as.map(a => ({ href: a.href, texts: [...new Set([...a.querySelectorAll('p,h1,h2,h3,h4,span')].map(e => e.innerText.trim()).filter(Boolean))], img: a.querySelector('img')?.src || null })));
(async () => {
  const { browser, ctx } = await launch(); const page = await ctx.newPage();
  for (const [name, url] of [['home2', 'https://www.brandguidelines.net/'], ['templates', 'https://www.brandguidelines.net/templates'], ['about', 'https://www.brandguidelines.net/about']]) {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.getByText('Reject', { exact: true }).click({ timeout: 4000 }).catch(() => {});
    const clicks = await exhaust(page);
    const cards = await extract(page);
    fs.writeFileSync(`${OUT}/${name}_cards.json`, JSON.stringify(cards, null, 1));
    fs.writeFileSync(`${OUT}/${name}.html`, await page.content());
    console.log(name, 'clicks', clicks, 'anchors', cards.length);
  }
  await browser.close();
})();
