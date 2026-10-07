// Shared browser helpers: stealth-ish context that passes Vercel's JS challenge.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
async function launch(opts = {}) {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--disable-blink-features=AutomationControlled', '--autoplay-policy=no-user-gesture-required'] });
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 }, ...opts });
  await ctx.addInitScript(() => Object.defineProperty(navigator, 'webdriver', { get: () => undefined }));
  return { browser, ctx };
}
// Navigate and wait until we are past the "Vercel Security Checkpoint" page.
async function gotoPast(page, url, timeout = 45000) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    const title = await page.title().catch(() => '');
    if (!/Security Checkpoint/i.test(title)) { await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {}); return true; }
    await page.waitForTimeout(1500);
  }
  return false;
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
module.exports = { launch, gotoPast, sleep };
