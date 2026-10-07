// Probe a URL: log JSON/API responses and save rendered HTML + screenshot.
const { chromium } = require(process.env.PW || 'playwright');
const fs = require('fs');
(async () => {
  const url = process.argv[2], out = process.argv[3];
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const log = [];
  page.on('response', async r => {
    const ct = r.headers()['content-type'] || '';
    log.push(`${r.status()} ${r.request().method()} ${ct.slice(0,30)} ${r.url()}`);
    if (ct.includes('json') || r.url().includes('_next/data') || r.url().includes('api')) {
      try { const b = await r.text(); fs.writeFileSync(`${out}/resp_${log.length}.txt`, r.url() + '\n' + b); } catch {}
    }
  });
  await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(3000);
  fs.writeFileSync(`${out}/page.html`, await page.content());
  await page.screenshot({ path: `${out}/shot.png` });
  fs.writeFileSync(`${out}/network.log`, log.join('\n'));
  await browser.close();
})();
