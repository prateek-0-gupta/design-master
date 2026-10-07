import {chromium} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:800}});
await p.goto('file:///home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/with_skill/outputs/index.html');await p.waitForTimeout(800);
console.log(await p.evaluate(()=>{const o=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.right>392&&r.width>0&&!e.closest('nav')&&!e.closest('.tabs'))o.push(e.tagName+'.'+e.className+' '+Math.round(r.right))});return o.slice(0,15).join('\n')}));
console.log(await p.evaluate(()=>[...document.querySelectorAll('a,button,input,summary')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&(r.height<44||r.width<44)&&getComputedStyle(e).position!=='absolute'}).map(e=>e.tagName+e.className+e.textContent.slice(0,20)+Math.round(e.getBoundingClientRect().height)).join('\n')));
await b.close();
