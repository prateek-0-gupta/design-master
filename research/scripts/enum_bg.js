// Enumerate brandguidelines.net: click "Load More" until it disappears, then extract every card.
const { launch, sleep } = require('./lib');
const fs = require('fs');
const OUT = __dirname + '/../raw/brandguidelines/_enum';
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const { browser, ctx } = await launch(); const page = await ctx.newPage();
  await page.goto('https://www.brandguidelines.net/', { waitUntil: 'networkidle', timeout: 60000 });
  await page.getByText('Reject', { exact: true }).click({ timeout: 5000 }).catch(() => {});
  let clicks = 0;
  for (let i = 0; i < 80; i++) {
    const btn = page.getByText(/^Load More$/i).first();
    if (!(await btn.isVisible().catch(() => false))) { await page.mouse.wheel(0, 3000); await sleep(1500); if (!(await btn.isVisible().catch(() => false))) break; }
    await btn.scrollIntoViewIfNeeded(); await btn.click(); clicks++; await sleep(2000);
    const n = await page.$$eval('a[href]', a => a.length); console.log('click', clicks, 'anchors', n);
  }
  for (let y = 0; y < 60; y++) { await page.mouse.wheel(0, 2500); await sleep(150); }
  await sleep(2000);
  fs.writeFileSync(OUT + '/home_full.html', await page.content());
  const cards = await page.$$eval('a[href]', as => as.map(a => {
    const texts = [...a.querySelectorAll('p, h1, h2, h3, h4, span')].map(e => e.innerText.trim()).filter(Boolean);
    const img = a.querySelector('img');
    const icons = [...a.querySelectorAll('[data-framer-component-type], svg')].map(e => e.getAttribute('data-framer-name') || '').filter(Boolean);
    let p = a, section = ''; while (p && !section) { p = p.parentElement; if (p && p.getAttribute) section = p.getAttribute('data-framer-name') || ''; }
    return { href: a.href, texts: [...new Set(texts)], img: img ? img.src : null, imgAlt: img ? img.alt : null, names: [...new Set([...a.querySelectorAll('[data-framer-name]')].map(e => e.getAttribute('data-framer-name')))], section, rect: (() => { const r = a.getBoundingClientRect(); return [Math.round(r.x), Math.round(r.y + scrollY), Math.round(r.width), Math.round(r.height)]; })() };
  }));
  fs.writeFileSync(OUT + '/home_cards.json', JSON.stringify(cards, null, 1));
  console.log('clicks', clicks, 'anchors', cards.length);
  await page.screenshot({ path: OUT + '/home_full.png', fullPage: true }).catch(e => console.log('ss fail', e.message));
  await browser.close();
})();
