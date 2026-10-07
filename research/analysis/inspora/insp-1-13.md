---
id: insp-1-13
source: inspora
category: Web
status: analyzed
title: "folder component"
creator: "@designbyaron"
styles: [corporate-clean, editorial-serif, micro-interaction]
patterns: [stacked-folder-tabs, scroll-driven-stack, hover-lift-sheet, rubber-stamp-label, numbered-step-list, mono-tab-labels]
mode: light
palette: ["#f3f3f3", "#fffffe", "#4f6de5", "#6787ee", "#91a3e3", "#d4d9ee", "#ef4452"]
type_families: ["Tiempos Headline / Newsreader-style serif (likely)", "Inter (likely)", "pixel-ish mono such as Space Mono / IBM Plex Mono (likely)"]
type_class: [editorial-serif, neo-grotesk, mono]
radius_px: [12, 8, 4]
motion: {durations_s: [0.27, 0.33, 0.5, 1.03], easing: [ease-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 7, craft: 8}
craft_signals: [trapezoid-tab-with-soft-shoulders, tab-offset-staggered-per-sheet, sheet-tint-steps-by-depth, stamp-rotated-minus-3deg, pixel-glyph-icons-per-step, serif-display-with-sans-body]
anti_patterns: [white-on-blue-at-aa-threshold, lilac-headline-line-fails-aa, red-cta-text-fails-aa]
---
# folder component — @designbyaron

## 1. Snapshot
- **Subject:** A 27.1 s, 3840×2160 (2× retina, about 1920 CSS px wide) screen recording of a "Runline" credit-union AI landing page. Four service rows (Connect, Secure, Deploy, Amplify) are drawn as paper sheets tucked into a big blue manila-style folder.
- **Why it's remarkable:** The folder metaphor is literal and also structural. Each step owns a folder tab, and scrolling or hovering fans the sheets out so the tab labels ("01 CONNECT", "02 SECURE"…) can be read like file dividers.

## 2. Composition & layout
- A centred container of about 1200 CSS px with 1 px hairline gutters at x≈195 and x≈1393 (in a 1600 px frame). The nav is 66 px tall: wordmark left, six links, and a red "GET STARTED" pill on the right.
- The hero copy is left-aligned in a 2-line serif headline with a tilted red "TRUE POTENTIAL" stamp inline, plus a 3-line grey sub-paragraph about 270 px wide.
- **Folder stack:** Four white sheets, each about 88 px tall. Each sheet is wider than the one above by about 30 px per side, which gives a forced-perspective fan. The sheets sit on a blue folder back (top, with a centred trapezoid tab) and a blue folder front (bottom, about 1130 px wide, slight outward-flared sides).
- **Inside each sheet:** A two-column grid. The left side has a step number, a pixel icon and a serif title. The right column, starting at about 60% of the width, holds 2 lines of grey body copy.

## 3. Typography
- **Display:** A high-contrast transitional serif with tight tracking (about −0.03 em), close to Tiempos Headline or Newsreader. The hero is about 36 CSS px with leading of about 1.05. Folder text "We Don't Sell You AI. / We Do The Work." is about 34 px. Its first line is lilac #d4d9ee and the second white, so tint creates a two-beat emphasis.
- **Row titles:** the same serif at about 24 px. Body is Inter-like at 14 px/1.45 in grey (≈#5f5f5f).
- **Mono:** Tab labels and the stamp use a squarish uppercase mono (Space Mono / Plex Mono feel) at about 13 px with letter-spacing of about 0.12 em. Step numbers "01–04" are about 10 px mono.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #4f6de5 | folder body, main brand blue | 52% |
| #f3f3f3 | page canvas | 24.5% |
| #6787ee | lighter folder layers (nearer = lighter) | 13.6% |
| #fffffe | paper sheets | 4.3% |
| #d4d9ee | lilac first line of folder headline | 3% |
| #91a3e3 | dimmed tab numerals | 2.7% |
| #ef4452 | CTA, stamps, pixel icons | <1% |

WCAG checks:
- White on #4f6de5 is 4.51:1, which only just passes AA.
- Lilac #d4d9ee on blue is 3.22:1 (large-text only, which is acceptable at 34 px).
- Tab numerals #91a3e3 on blue are 1.84:1 and fail.
- Red stamp text on #f3f3f3 is 3.77:1, and white on the red CTA is 3.74:1. Both fail at small sizes.
- Grey body #5f5f5f on #f3f3f3 is 5.75:1 and passes.

## 5. Depth & material
- There are no drop shadows. Depth comes from three tints of blue (#4f6de5 → #6787ee → lighter), white sheets peeking out as 10–15 px strips between folder layers, and a slight perspective widening of lower sheets.
- The folder tabs are trapezoids with about 12 px eased shoulders, not hard 45° bevels.
- The stamp is a 2 px red outline with radius of about 6 px, rotated about −3°, like an ink stamp.

## 6. Components & patterns
- **Folder-tab section dividers:** each tab carries a number, a pixel icon and a mono label.
- **Stacked file sheets:** these serve as a numbered feature list.
- **Rubber-stamp highlight:** used inline in the H1 and as a hover tooltip ("03 · DEPLOY" appears above the cursor at t≈19.6 s).
- A fixed sound-toggle button at bottom-left and a back-to-top square at bottom-right, both 32 px with 1 px borders.
- A small handwritten "tap the folder!" annotation with an arrow (frame t≈10.5 s) acts as an onboarding hint.

## 7. Motion
Measured: 27.09 s at 60 fps. motion_fraction is 0.23, there are 17 segments with a median of 0.27 s, and the clip is not a seamless loop.
- **Sheet lift on hover:** short bursts of 0.27 s, 0.33 s and 0.37 s (11.07–12.43 s). peak_at is 0.15–0.31, i.e. ease-out.
- **Folder open/zoom transitions:** longer 1.03 s segments at 22.33 s and 24.13 s, with peak_at 0.02 and 0.15, which is a strong ease-out (a fast snap that settles).
- **Behaviour:** Between t=10.5 s and t=13.6 s the view zooms into the folder and the sheets compress into thin strips that show only their tabs. Tabs then slide laterally (frames 16.6–19.6 s) so each label shows in turn.
- One ease-in segment of 0.63 s at 17.17 s reads as a sheet being pulled down into the folder.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the "Runline" wordmark with a red striped flag mark;
- a red/blue "official paperwork" palette;
- stamps and pixel glyphs that give a bureaucracy-as-brand tone suited to credit unions.

## 9. UX
- The metaphor maps cleanly to a four-step process, and the numbered tabs keep order clear even when the sheets collapse.
- The hover stamp gives clear feedback.
- **Risks:**
  - Hidden content (only tabs visible) needs a keyboard and tap equivalent.
  - The 14 px grey body copy inside the sheets is small at a 1920 px viewport.
  - Several labels sit under the AA threshold.

## 10. Craft signals
- Each sheet is about 30 px wider per side than the one above, and the tabs stagger left → right (Connect at about 25% of x, Secure at 45%, Deploy at 72%), like real divider tabs.
- Three-step blue tint ramp encodes z-depth with no shadows.
- Tab shoulders use eased curves (about 12 px), and the same shape is reused for the folder back tab and the front pocket.
- The stamp motif repeats in the H1 and in the hover tooltip, at the same −3° rotation and the same 2 px stroke.
- Pixel-grid icons (about 5×5 dots) per step are in red on white and white on blue.

## 11. Reproduction recipe
```css
:root{--canvas:#f3f3f3;--paper:#fffffe;--blue:#4f6de5;--blue-2:#6787ee;--lilac:#d4d9ee;--red:#ef4452;
  --serif:"Tiempos Headline","Newsreader",Georgia,serif;--sans:"Inter",system-ui;--mono:"Space Mono",ui-monospace;}
.tab{--w:220px;height:28px;width:var(--w);background:var(--blue);
  clip-path:path('M0 28 C12 28 14 0 30 0 H190 C206 0 208 28 220 28 Z');
  font:600 13px/28px var(--mono);letter-spacing:.12em;color:#fff;text-transform:uppercase;padding-left:40px}
.sheet{background:var(--paper);border-radius:12px 12px 0 0;margin-inline:calc(var(--i)*-30px);
  transition:transform .33s cubic-bezier(.2,.8,.2,1)}
.sheet:hover{transform:translateY(-18px)}
.stamp{display:inline-block;border:2px solid var(--red);border-radius:6px;color:var(--red);
  font:700 13px var(--mono);letter-spacing:.12em;padding:2px 8px;transform:rotate(-3deg)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A confident two-colour system, and the serif plus mono pairing feels official without being stiff. |
| Originality | 8 | The folder-as-feature-list with real divider tabs is a fresh literal metaphor for a fintech page. |
| Usability | 7 | Clear sequence and good hover feedback. Collapsed state hides copy and several labels fail AA. |
| Craft | 8 | Consistent tab geometry, stagger and tint ramp. The stamp motif is reused precisely. |
