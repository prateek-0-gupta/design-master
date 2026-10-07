---
id: insp-onboarding-screen
source: inspora
category: Product
status: analyzed
title: "onboarding screen"
creator: "@FarzadGodarz"
styles: [soft-3d, playful-rounded, micro-interaction]
patterns: [onboarding-carousel, illustrated-hero-card, path-progress-indicator, blur-in-headline, pill-nav-buttons, leaderboard-preview, auth-cta-stack]
mode: light
palette: ["#ffffff", "#fde9c8", "#fef8ee", "#f1c475", "#010101", "#2d2e31", "#7a7a7a", "#b5b7b9"]
type_families: ["SF Pro Display / Inter-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [9999, 40, 32, 24]
motion: {durations_s: [0.9, 1.4, 1.13, 1.37, 0.17], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 7, originality: 6, usability: 6, craft: 7}
craft_signals: [progress-as-connected-path, per-word-blur-reveal, single-hue-illustration-set, dark-pill-nav-pair, ghost-back-button-on-first-step, eyebrow-plus-two-line-title]
anti_patterns: [low-contrast-body-text, near-invisible-card-labels]
---
# onboarding screen — @FarzadGodarz

## 1. Snapshot
- **Subject:** A 19.75 s, 1080×1350 screen recording of a four-step onboarding for a vocabulary/flashcard app, shown in an iPhone frame on white. The steps are Smart Learning, Compete & Achieve, Global Ranking and a "Ready to Master It?" sign-up screen.
- **Why it's remarkable:** The page dots are replaced by a **connected path of milestone nodes** (bookmark, star, "#1"). Each step draws the next orange segment, so progress reads as a journey rather than a pager.

## 2. Composition & layout
- The phone is about 560 px wide (x≈260→820), centred, with about 40% white margin around it. Inside it, every step uses the same three bands:
  - **Illustration card:** y≈180→810, about 488×630 px, radius about 32 px, with a warm cream gradient fill.
  - **Text block:** centred, about 80 px below the card.
  - **Nav bar:** about 76 px tall at y≈1130.
- The nav bar is a 110×76 px black back pill on the left, a light-grey (#f4f4f4) track holding the path progress in the middle, and a 110×76 px black forward pill on the right.
- On step 1 the back pill is greyed (#c4c4c4), which correctly signals that there is no previous step.
- The final screen drops the card for a free-floating 3D trophy (about 180 px) and stacks the two CTAs, each about 230×36 px at sheet scale and roughly 460×72 px real.

## 3. Typography
- Neo-grotesk, close to SF Pro Display. The title is about 44 px Semibold/Bold, set on two lines with leading of about 1.15 and slightly negative tracking.
- **Eyebrow:** about 18 px Regular, all caps, #2d2e31 (e.g. "GLOBAL RANKING").
- **Body:** about 17 px Regular, centred, grey #7a7a7a, two lines of about 50 characters.
- **Leaderboard rows:** about 24 px Medium ("#1 Farzad"), with numerals about 20 px.
- The ratio from title to body is about 2.6×. Hierarchy comes from size and weight; colour is only black and grey.

## 4. Colour
| Hex | Role | Share (key) |
|---|---|---|
| #ffffff | screen / canvas | 75% |
| #fde9c8 | illustration card warm fill | 8% |
| #fef8ee | inner leaderboard sheet | 5% |
| #f1c475 → deep orange (~#f5a623) | medals, path nodes, coins | 2% |
| #010101 | nav pills, primary CTA | 2% |
| #2d2e31 | headings | 1.5% |
| #7a7a7a | body copy | 1% |
| #b5b7b9 | "Winner Board" label, iPhone frame | 3% |

WCAG checks:
- Black heading on white: 20.9:1.
- Body #7a7a7a on white: **4.29:1, which fails AA-normal** at 17 px.
- "Winner Board" #b5b7b9 on #fef8ee: **1.9:1**.
- Heading #2d2e31 on the cream card: 11.4:1.
- Orange #f1c475 on white: 1.63:1, which is fine because it is decorative only.

The scheme is monochrome-orange, with all the warmth confined to the illustration card.

## 5. Depth & material
- The illustrations are soft-3D, clay-like medals with inner rings (concentric 3-tone orange discs) and a matte, low-specular finish.
- The card itself has an inner vignette: the edges are deeper (#f1c475 tint) and the centre is lighter, which reads as a glowing lightbox.
- The leaderboard sheet sits on the card as a frosted white panel (#fef8ee, about 90% opacity) with a 24 px radius.
- No drop shadows appear on the UI chrome.

## 6. Components & patterns
- **Flashcard stack:** the "Soccer (n)" card is rotated about −12° over a back card, with category chips ("Billiards", "Football") as 1 px-bordered white pills.
- **Leaderboard rows:** pills about 400×60 px. The #1 row is highlighted with a #fde9c8 fill; the other rows are faded.
- **Path progress:** three orange nodes about 30 px across, joined by 6 px curved strokes. The current node gets a ring and the future nodes are grey.
- **Auth stack:** a black "Create Account" pill, an outlined "Login" pill, and legal text at about 11 px with bold links.

## 7. Motion
Measured: duration 19.75 s at 30 fps, `motion_fraction` 0.27, 7 segments, median 0.9 s, with no seamless loop.
- **Step transitions:** 3.53–4.93 s (1.40 s, peak 0.27 → ease-out) and 13.93–15.30 s (1.37 s, ease-out). The 9.07–10.20 s transition is 1.13 s, symmetric ease-in-out.
- **Tap presses:** 0.17 s and 0.13 s at 2.67 and 8.10 s. These are the ring ripples visible on the → button in frame 2.
- **Choreography (from frames):**
  - The headline reveals **word by word with a Gaussian-blur-to-sharp** fade. In the key frame "Climb the" is sharp, "Global" is half-blurred and "Rankings" is fully blurred.
  - The body copy follows at about 30% opacity.
  - The illustration cross-fades and slides up by about 40 px.
  - The leaderboard rows rise in stagger with a count-up on the numbers (4,509 → 12,848).
  - The path segment grows toward the next node.
- Exit is a whole-screen fade to white at about 14.3 s before the auth screen.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a single amber hue for all achievement objects;
- a coin glyph beside the numbers;
- black pills as the only interactive colour.

## 9. UX
- **Strengths:**
  - Four screens is the right length for onboarding.
  - The path indicator tells the user both how many steps there are and what each one is about (icon per node).
  - The disabled back button on step 1 is correct.
- **Risks:**
  - There is no Skip.
  - The grey body copy fails AA.
  - The faded leaderboard rows (#3 and #4 sit at about 1.5:1) are illegible as content, though they serve as decoration.
  - The forward arrow is the only way to advance in the footage; swipe support is not shown.

## 10. Craft signals
- The progress nodes carry semantic icons (bookmark, star, #1) that match each step's illustration.
- The headline blur-reveal is staggered per word rather than per line.
- The back and forward pills are identical 110×76 px shapes, so the bar is symmetric.
- The illustration card radius (~32 px) is nested inside the device screen radius (~55 px), and the inner sheet is ~24 px, giving consistent concentric reduction.
- Numbers count up on the leaderboard reveal.

## 11. Reproduction recipe
```css
:root{--bg:#fff;--card:#fde9c8;--sheet:#fef8ee;--amber:#f5a623;--amber-soft:#f1c475;
  --ink:#010101;--text:#2d2e31;--muted:#6b6b6b;/* darkened from #7a7a7a for AA */
  --r-card:32px;--r-sheet:24px;--r-pill:9999px}
.hero-card{border-radius:var(--r-card);background:radial-gradient(80% 70% at 50% 45%,#fff7ea 0%,var(--card) 70%,var(--amber-soft) 120%)}
.nav-btn{width:110px;height:76px;border-radius:var(--r-pill);background:var(--ink);color:#fff}
.nav-btn:disabled{background:#c4c4c4}
.path path{stroke:var(--amber);stroke-width:6;stroke-linecap:round;stroke-dasharray:var(--len);stroke-dashoffset:var(--len);transition:stroke-dashoffset 1.1s cubic-bezier(.2,.8,.2,1)}
.title .w{display:inline-block;filter:blur(8px);opacity:0;animation:wordIn .6s cubic-bezier(.2,.8,.2,1) forwards;animation-delay:calc(var(--i)*90ms)}
@keyframes wordIn{to{filter:blur(0);opacity:1}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 7 | Cohesive single-hue 3D illustration set with a calm white frame, though it is fairly conventional. |
| Originality | 6 | The path progress indicator is the fresh bit; the rest is a standard carousel. |
| Usability | 6 | Clear steps and back/forward controls, but no skip and the body grey fails AA. |
| Craft | 7 | Per-word blur reveal, count-ups and nested radii are careful touches. |
