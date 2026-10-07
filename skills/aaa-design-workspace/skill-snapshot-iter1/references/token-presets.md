# Token presets

Four complete `:root` systems. All text pairs were checked with `scripts/contrast.py`, and the ratios are noted in comments. Copy the closest preset, rename the accent to fit the brand, then re-run the contrast check on any colour you change.

Shared rules in every preset:
- text-1 ≥ 12:1, text-2 ≥ 7:1 and text-3 ≥ 4.5:1 on canvas and surface-1;
- control borders ≥ 3:1;
- accent-ink is the accent used **as text**;
- `--on-accent` is the text colour that sits **on** an accent fill.

## Contents
1. Neutral Swiss: light product UI, SaaS, fintech, dashboards
2. Dark Premium: AI, dev tools, media, fintech dark
3. Editorial Warm: portfolio, culture, brand pages, research
4. Playful Soft: consumer, education, onboarding
5. Shared scale (type, space, radius, motion) and the reduced-motion block
6. Tailwind mapping

---

## 1. Neutral Swiss (light)

```css
:root {
  /* surfaces */
  --canvas:#ffffff; --surface-1:#f7f7f8; --surface-2:#f0f0f2; --surface-3:#e7e7ea;
  --hairline:rgb(17 17 19 / .08); --border-control:#8a8a93;          /* 3.42:1 on #fff */
  /* text */
  --text-1:#111113;   /* 18.9:1 on #fff */
  --text-2:#4a4a50;   /*  8.8:1 */
  --text-3:#6b6b72;   /*  5.3:1 on #fff, 4.8:1 on #f4f4f5 */
  /* accent (cobalt) */
  --accent:#2747d6; --accent-ink:#1d3bb8; --on-accent:#ffffff;          /* 7.1:1 both ways */
  --accent-soft:#e9edfc;                                                  /* chip/selection fill */
  /* semantic: fill + ink (ink is for text on canvas) */
  --success:#16a34a; --success-ink:#117f3a;                               /* 4.55:1 on #f2f2f2 */
  --warning:#f5a524; --warning-ink:#8a5300;
  --danger:#e5484d;  --danger-ink:#b4232a;
  /* elevation */
  --shadow-1:0 1px 2px rgb(17 17 19/.05), 0 1px 1px rgb(17 17 19/.03);
  --shadow-2:0 1px 2px rgb(17 17 19/.04), 0 8px 24px -6px rgb(17 17 19/.10);
  --highlight:inset 0 1px 0 rgb(255 255 255/.7);
  /* type */
  --font-sans:"Inter","InterVariable",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-mono:"JetBrains Mono","Geist Mono",ui-monospace,"SF Mono",Menlo,monospace;
  --radius-1:8px; --radius-2:14px; --radius-pill:9999px;
}
```
Signature-friendly layers: hairline/technical details, a physical metaphor (receipt, card, stamp), and a dark hero band that uses the Dark Premium tokens locally.

## 2. Dark Premium

```css
:root {
  --canvas:#0b0b0d; --surface-1:#141417; --surface-2:#1c1c20; --surface-3:#26262b;  /* elevation = lighter */
  --hairline:rgb(255 255 255/.08); --border-control:#6e6e78;              /* 3.9:1 on canvas */
  --text-1:#f5f5f7;   /* 18.1:1 on canvas */
  --text-2:#a1a1aa;   /*  7.7:1 on canvas */
  --text-3:#8b8b94;   /*  5.4:1 on surface-1, 5.0:1 on surface-2 */
  --accent:#b4a5ff; --accent-ink:#b4a5ff; --on-accent:#0b0b0d;           /* 9.2:1 both ways */
  --accent-soft:rgb(180 165 255/.12);
  --success:#4ade80; --success-ink:#4ade80;                               /* 10.9:1 on #1d1d1d */
  --warning:#fbbf24; --warning-ink:#fbbf24;
  --danger:#ff8b6b;  --danger-ink:#ff8b6b;                                /* 8.6:1 */
  --shadow-1:none; --shadow-2:0 0 0 1px var(--hairline), 0 12px 32px -8px rgb(0 0 0/.6);
  --highlight:inset 0 1px 0 rgb(255 255 255/.06);
  --glow:0 0 0 1px rgb(180 165 255/.25), 0 20px 60px -10px rgb(180 165 255/.35);
  --font-sans:"Inter","Geist",ui-sans-serif,system-ui,sans-serif;
  --font-mono:"Geist Mono","JetBrains Mono",ui-monospace,monospace;
  --radius-1:10px; --radius-2:16px; --radius-pill:9999px;
  color-scheme: dark;
}
```
Rules for this preset:
- Elevation comes from surface steps, never from drop shadows alone.
- Keep saturation inside one hero object (orb, shader, photo).
- Avoid pure #fff text on large display sizes: #f5f5f7 halates less.

## 3. Editorial Warm

```css
:root {
  --canvas:#f6f3ee; --surface-1:#efebe4; --surface-2:#e6e0d6; --surface-3:#1c1917;  /* surface-3 = ink band */
  --hairline:rgb(28 25 23/.12); --border-control:#857c74;                /* 3.7:1 */
  --text-1:#1c1917;   /* 15.8:1 on canvas */
  --text-2:#57534e;   /*  6.9:1 */
  --text-3:#6b645e;   /*  5.3:1 */
  --accent:#b3401f; --accent-ink:#b3401f; --on-accent:#ffffff;           /* 5.2:1 on canvas, 5.7:1 white on it */
  --accent-soft:#f3dfd5;
  --success:#2f6b3a; --warning:#8a5a00; --danger:#a3271b;
  --shadow-1:0 1px 0 rgb(28 25 23/.06); --shadow-2:0 2px 4px rgb(28 25 23/.04), 0 18px 40px -12px rgb(60 40 20/.18);
  --highlight:inset 0 1px 0 rgb(255 255 255/.5);
  --font-display:"Instrument Serif","PP Editorial New","Tiempos Headline",Georgia,serif;
  --font-sans:"Inter","Neue Haas Grotesk Text",ui-sans-serif,system-ui,sans-serif;
  --font-mono:"JetBrains Mono",ui-monospace,monospace;
  --radius-1:4px; --radius-2:10px; --radius-pill:9999px;
}
```
Rules for this preset:
- Use serif for display only (≥ 32px). Italic is for emphasis inside a headline.
- Use the sans for UI and body, and mono caps for indexes ("01 — Work").
- Use 0px radius for images and "paper" elements.

## 4. Playful Soft

```css
:root {
  --canvas:#fffaf2; --surface-1:#ffffff; --surface-2:#f6efff; --surface-3:#eaf8f1;
  --hairline:rgb(26 21 48/.08); --border-control:#8f86ac;                /* 3.3:1 */
  --text-1:#1a1530;   /* 16.9:1 */
  --text-2:#4b4566;   /*  8.6:1 */
  --text-3:#6a6485;   /*  5.4:1 */
  --accent:#5b2ee0; --accent-ink:#5b2ee0; --on-accent:#ffffff;           /* 6.9:1 / 7.2:1 */
  /* candy fills always take dark ink text */
  --candy-yellow:#ffd84d; --candy-lilac:#b9a7ff; --candy-mint:#7ee0b0;   /* text-1 on them: 12.7 / 8.4 / 11.0 */
  --shadow-1:0 1px 0 rgb(26 21 48/.06);
  --shadow-2:0 2px 0 rgb(26 21 48/.08), 0 16px 32px -10px rgb(91 46 224/.25);   /* hue-tinted */
  --highlight:inset 0 1px 0 rgb(255 255 255/.8);
  --font-sans:"Plus Jakarta Sans","Figtree","Nunito Sans",ui-rounded,system-ui,sans-serif;
  --font-mono:"JetBrains Mono",ui-monospace,monospace;
  --radius-1:12px; --radius-2:24px; --radius-3:32px; --radius-pill:9999px;
}
```
Rules for this preset:
- Never put white text on candy fills. Use `--text-1`, or an ink of the candy's own hue, e.g. `color-mix(in oklab, var(--candy-lilac) 25%, #000)`.

---

## 5. Shared scale (use with any preset)

```css
:root {
  /* type scale — app ratio 1.2; for marketing pages swap display sizes for the clamp() values */
  --fs-xs:12px; --fs-sm:14px; --fs-base:16px; --fs-md:19px; --fs-lg:23px; --fs-xl:28px; --fs-2xl:34px;
  --fs-display:clamp(2.5rem, 4.2vw + 1rem, 4.75rem);   /* 40 → 76px */
  --fs-hero:clamp(3rem, 7vw + .5rem, 7.5rem);          /* poster/type-as-image only */
  --lh-tight:1.04; --lh-snug:1.25; --lh-body:1.55;
  --tr-display:-0.028em; --tr-heading:-0.018em; --tr-body:0; --tr-caps:0.08em;
  /* space (4px base) */
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px; --s-8:64px; --s-9:96px; --s-10:128px;
  /* layout */
  --container:1240px; --measure:68ch; --gutter:24px;
  --margin:clamp(16px, 4vw, 64px);
  /* motion (measured median of 1,368 reference transitions = 0.33s) */
  --dur-1:120ms;  /* press, hover tint */
  --dur-2:200ms;  /* small state change, toggle */
  --dur-3:320ms;  /* container morph, menu open */
  --dur-4:560ms;  /* page / shared element */
  --dur-5:900ms;  /* scene, hero entrance */
  --ease-out:cubic-bezier(.2,.8,.2,1);
  --ease-in-out:cubic-bezier(.65,0,.35,1);
  --ease-in:cubic-bezier(.5,0,.75,0);      /* exits and falling only */
  --spring:linear(0, .45 12%, .86 25%, 1.02 38%, 1.04 47%, 1 62%, .995 80%, 1); /* gentle overshoot */
  --focus-ring:0 0 0 2px var(--canvas), 0 0 0 4px var(--accent-ink);
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration:1ms !important; animation-iteration-count:1 !important;
    transition-duration:120ms !important; transition-property:opacity, color, background-color, border-color !important;
    scroll-behavior:auto !important; }
}
:focus-visible { outline:none; box-shadow:var(--focus-ring); border-radius:inherit; }
body { font-family:var(--font-sans); font-size:var(--fs-base); line-height:var(--lh-body); color:var(--text-1);
  background:var(--canvas); -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; font-feature-settings:"ss01","cv11"; }
.num { font-variant-numeric:tabular-nums; }
```

## 6. Tailwind mapping (v3 `theme.extend` or v4 `@theme`)

```js
// tailwind.config.js (v3)
theme: { extend: {
  colors: { canvas:'var(--canvas)', s1:'var(--surface-1)', s2:'var(--surface-2)', s3:'var(--surface-3)',
    t1:'var(--text-1)', t2:'var(--text-2)', t3:'var(--text-3)', accent:'var(--accent)', 'accent-ink':'var(--accent-ink)', hairline:'var(--hairline)' },
  borderRadius: { 1:'var(--radius-1)', 2:'var(--radius-2)' },
  transitionTimingFunction: { out:'var(--ease-out)', 'in-out':'var(--ease-in-out)' },
  transitionDuration: { 1:'120ms', 2:'200ms', 3:'320ms', 4:'560ms' },
  letterSpacing: { display:'-0.028em', heading:'-0.018em', caps:'0.08em' },
}}
```
```css
/* Tailwind v4 */
@theme { --color-canvas: #ffffff; --color-t1: #111113; --color-t2: #4a4a50; --color-t3: #6b6b72; --color-accent: #2747d6;
  --radius-card: 14px; --ease-out: cubic-bezier(.2,.8,.2,1); }
```
