import {chromium} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/with_skill/outputs/index.html');await p.waitForTimeout(2200);
await p.screenshot({path:'hero.png'});await b.close();
