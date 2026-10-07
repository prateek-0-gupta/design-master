const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs');
(async () => {
  const url = process.argv[2], out = process.argv[3];
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  let n = 0;
  page.on('request', r => { const u = r.url(); if (!/\.(png|jpe?g|webp|woff2?|css|js|mp4|svg)(\?|$)/.test(u) && !u.includes('_rsc')) console.log('REQ', r.method(), u, (r.postData()||'').slice(0,300)); });
  page.on('response', async r => { const u = r.url(); if (r.request().method()==='POST' || u.includes('api')) { try { fs.writeFileSync(`${out}/r${n++}.txt`, u + '\n' + JSON.stringify(r.request().headers()) + '\n' + (r.request().postData()||'') + '\n----\n' + await r.text()); } catch {} } });
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);
  for (let i = 0; i < 6; i++) { await page.mouse.wheel(0, 4000); await page.waitForTimeout(1500); }
  console.log('links', await page.$$eval('a[href^="/posts/"]', a => new Set(a.map(x => x.getAttribute('href'))).size));
  await browser.close();
})();
