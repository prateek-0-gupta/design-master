const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--disable-blink-features=AutomationControlled'] });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  await ctx.addInitScript(() => Object.defineProperty(navigator, 'webdriver', { get: () => undefined }));
  const page = await ctx.newPage();
  await page.goto('https://www.inspora.design/api/posts?view=latest', { timeout: 60000 });
  for (let i=0;i<8;i++){ await page.waitForTimeout(3000); const t = await page.evaluate(()=>document.body.innerText.slice(0,200)); console.log(i, t.replace(/\n/g,' ')); if (t.startsWith('{')) break; }
  console.log((await ctx.cookies()).map(c=>c.name));
  await browser.close();
})();
