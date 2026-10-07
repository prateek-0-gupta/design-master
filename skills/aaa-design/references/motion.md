# Motion

## Measured house style (1,368 transitions from 261 reference videos)

| Measure | Value |
|---|---|
| Median duration | 0.33s |
| Middle half of durations | 0.2–0.57s (p10 0.1s, p90 0.93s) |
| Ease-out (fast start, decelerating) | 44% |
| Symmetric ease-in-out | 37% |
| Ease-in | 16% |
| Linear | 2% |
| Where motion energy peaks | 38% of the way through, on median |
| Seamless ambient loops | 45% (the rest jump at the loop point) |
| CSS transitions on real sites | 0.2s (most common), then 0.3, 0.15, 0.4s |

## Tokens

```css
--dur-1:120ms;  /* press feedback, hover tint, checkbox */
--dur-2:200ms;  /* toggle, chip select, small state */
--dur-3:320ms;  /* menu/popover open, container morph, tab content */
--dur-4:560ms;  /* page transition, shared-element, modal */
--dur-5:900ms;  /* hero entrance, scene change, camera move */
--ease-out:cubic-bezier(.2,.8,.2,1);      /* default for anything entering or responding */
--ease-in-out:cubic-bezier(.65,0,.35,1);  /* moving between two resting places */
--ease-in:cubic-bezier(.5,0,.75,0);       /* exits, dismissals, things falling */
--spring:linear(0,.45 12%,.86 25%,1.02 38%,1.04 47%,1 62%,.995 80%,1);
```

## Choreography rules (each observed in top examples)

1. **Every animation signals a state change.** Decorative infinite loops were a recurring anti-pattern; ambient motion is slow (≥ 3s), seamless and pausable.
2. **Open slower than you close, by about 1.5–3×.** Measured pairs: menu 0.37s / 0.13s, receipt 0.6s / 0.2s, action menu 0.3s / 0.2s.
3. **Pick the easing by what the motion represents.**
   - Entries and responses: ease-out.
   - Things falling or dismissed: ease-in.
   - Machines (printers, conveyor belts): linear.
   - Tactile feedback: a ≤ 0.6s spring.
4. **Scale duration with distance and importance.** A tap is about 0.2s, an in-panel swap about 0.45s, a shared-element lift about 1s.
5. **Container first, content second.** When a button morphs into a panel, the container animates over `--dur-3`. Its content then fades in, starting 60–100ms later:
   ```css
   .panel[data-open] .content{animation:in var(--dur-3) var(--ease-out) 80ms both}
   @keyframes in{from{opacity:0;filter:blur(6px);transform:scale(.97)}}
   ```
6. **Blur rather than slide when swapping text or values.** Content swaps cross-blur, at about 6–12px, instead of travelling.
7. **Stagger lists by 40–80ms per item,** keeping the total under 400ms.
8. **Feedback within 100ms:** `:active{transform:scale(.97)}` or a 1–2px y-shift, then release over `--dur-2`.
9. **Numbers roll, they don't jump.** Use tabular figures so the width stays fixed.
10. **Thinking and loading motion is slow and never snaps.** Pair it with staged status text that changes every 2–5s ("Reading 12 files…" → "Drafting…").
11. **Shared-element continuity.** The thing tapped becomes the thing shown; use the View Transitions API where supported:
    ```css
    @view-transition{navigation:auto} ::view-transition-group(*){animation-duration:var(--dur-4);animation-timing-function:var(--ease-out)}
    ```

## Reduced motion (required; none of the 261 reference videos demonstrated it)

```css
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:1ms!important;animation-iteration-count:1!important;
    transition-duration:120ms!important;transition-property:opacity,color,background-color,border-color!important;scroll-behavior:auto!important}
  .parallax,.marquee,.autoplay{transform:none!important;animation:none!important}
}
```
In JS, read `matchMedia('(prefers-reduced-motion: reduce)').matches` and skip springs, scroll-linked effects and auto-advancing carousels.

## Springs in JS (when CSS isn't enough)

```js
// critically-damped-ish spring; settles ≈0.5s. k≈240, ζ chosen for slight overshoot.
function spring(from, to, onUpdate, {k=240, c=22, m=1}={}){ let x=from, v=0, last=performance.now();
  function step(t){ const dt=Math.min((t-last)/1000,1/30); last=t; const a=(-k*(x-to)-c*v)/m; v+=a*dt; x+=v*dt; onUpdate(x);
    if(Math.abs(v)>0.001||Math.abs(x-to)>0.001) requestAnimationFrame(step); else onUpdate(to); }
  requestAnimationFrame(step); }
```
