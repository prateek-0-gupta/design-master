// Enumerate every Inspora post across views (latest, featured) x categories via /api/posts cursor pagination.
// Runs fetch() inside a real browser context so the Vercel challenge cookie applies.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs');
const OUT = __dirname + '/../raw/inspora/_api';
fs.mkdirSync(OUT, { recursive: true });
const CATS = ['All', 'Web', 'Branding', 'Product', 'Motion', 'Illustration', '3D', 'Print'];
const VIEWS = ['latest', 'featured'];
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--disable-blink-features=AutomationControlled'] });
  const ctx = await browser.newContext({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  await ctx.addInitScript(() => Object.defineProperty(navigator, 'webdriver', { get: () => undefined }));
  const page = await ctx.newPage();
  await page.goto('https://www.inspora.design/api/posts?view=latest', { timeout: 60000 });
  await page.waitForTimeout(3000);
  const posts = {}; const membership = {}; const log = [];
  for (const view of VIEWS) for (const cat of CATS) {
    let cursor = null, pageNo = 0, count = 0;
    do {
      const q = new URLSearchParams({ view }); if (cat !== 'All') q.set('category', cat); if (cursor) q.set('cursor', cursor);
      const url = '/api/posts?' + q;
      let data = null;
      for (let attempt = 0; attempt < 5 && !data; attempt++) {
        const res = await page.evaluate(async u => { const r = await fetch(u, { headers: { accept: 'application/json' } }); return { s: r.status, t: await r.text() }; }, url);
        try { const j = JSON.parse(res.t); if (j.items) data = j; else throw new Error(res.t.slice(0, 120)); }
        catch (e) { log.push(`retry ${attempt} ${url} ${res.s} ${e.message}`); await sleep(4000 * (attempt + 1)); if (attempt >= 1) { await page.goto('https://www.inspora.design/api/posts?view=latest'); await page.waitForTimeout(4000); } }
      }
      if (!data) { log.push(`FAILED ${url}`); break; }
      fs.writeFileSync(`${OUT}/${view}_${cat}_${pageNo}.json`, JSON.stringify(data));
      for (const it of data.items) { posts[it.slug] = { ...(posts[it.slug] || {}), ...it }; (membership[it.slug] ||= new Set()).add(`${view}:${cat}`); }
      count += data.items.length; cursor = data.nextCursor; pageNo++;
      await sleep(1200);
    } while (cursor);
    console.log(view, cat, 'pages', pageNo, 'items', count, 'unique so far', Object.keys(posts).length);
  }
  const m = {}; for (const k in membership) m[k] = [...membership[k]];
  fs.writeFileSync(`${OUT}/posts.json`, JSON.stringify(posts, null, 1));
  fs.writeFileSync(`${OUT}/membership.json`, JSON.stringify(m, null, 1));
  fs.writeFileSync(`${OUT}/enum.log`, log.join('\n'));
  console.log('done', Object.keys(posts).length, 'log lines', log.length);
  await browser.close();
})();
