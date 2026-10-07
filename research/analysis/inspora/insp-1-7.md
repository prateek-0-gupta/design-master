---
id: insp-1-7
source: inspora
category: Product
status: analyzed
title: "X money"
creator: "@alexabraham"
styles: [micro-interaction, soft-3d, corporate-clean]
patterns: [card-stack-shuffle, payment-activity-card, overlapping-avatar-pair, verified-badge-inline, timestamp-bottom-right, auto-advancing-carousel]
mode: light
palette: ["#e4e4e6", "#f5f5f5", "#111111", "#8c8c8c", "#1d9bf0", "#a19a9e"]
type_families: ["Chirp / GT America-style grotesk (likely)"]
type_class: [grotesk]
radius_px: [28, 9999]
motion: {durations_s: [0.3, 0.33, 0.27], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [stack-peek-two-cards, rotated-back-cards-3deg, verb-in-grey-names-in-bold, avatar-ring-overlap, floor-shadow-ellipse, constant-cadence-0-85s]
anti_patterns: [low-contrast-timestamp, quote-text-below-aa]
---
# X money — @alexabraham

## 1. Snapshot
- **Subject:** A 6.9 s, 1240×1240 loop of a payment-activity card stack ("$4,200 · james paid jackson · 'rent' · 3h") that shuffles every ~0.85 s through four transactions.
- **Why it's remarkable:** It turns a social payments feed into a single tactile object: the stack itself is the feed, and each swap is a physical flick rather than a list scroll.

## 2. Composition & layout
- One card centred on a #e4e4e6 field, about 665×285 px (≈54% of frame width), sitting slightly above the optical centre (top edge y≈478, bottom y≈762).
- Two back cards peek out below and right by ~15–75 px, rotated roughly +3° and −4°, giving the "pile of receipts" read without showing their content.
- Inside the card: 40 px left padding, amount top-left at y≈550, the "name paid name" line at ~95 px below, quote line at ~150 px below; avatar pair top-right, timestamp bottom-right aligned to the quote baseline. A clean two-corner diagonal (amount ↖, time ↘).

## 3. Typography
- A neo-grotesk with a slightly squarish, compact feel, consistent with X's Chirp (GT America derivative). Amount is ~60 px Bold with tight tracking (≈−0.02 em) and lining figures.
- Sentence line is ~26 px: names in Bold #111, the verb "paid" in Regular grey — the grammar is carried by weight and value, which reads instantly.
- Memo is ~24 px Regular grey inside curly quotes (“ ”, real typographic quotes, not straight). Timestamp "3h" is ~24 px grey.
- Scale: 60 / 26 / 24 — essentially one display size and one text size.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e4e4e6 | stage background | ~90% |
| #f5f5f5 | card face (with a subtle white→grey sheen) | ~8% |
| #111111 | amount, names | <1% |
| #8c8c8c | verb, memo, timestamp | <1% |
| #1d9bf0 | verified badge | trace |
| #a19a9e | avatar/shadow mid-tones | ~1% |

WCAG: #111 on #f7f7f7 = **17.63:1**. Grey #8c8c8c on #f7f7f7 = **3.14:1** (passes large only; the 24–26 px text is borderline "large" only if bold, so it technically fails AA). Lighter "rent" on back cards (#a0a0a0) is 2.44:1 but those are decorative. Card vs stage is 1.19:1 — separation relies entirely on shadow.

## 5. Depth & material
- Cards have a soft, wide ambient shadow (~40 px blur, ~6% black) plus a lighter floor ellipse beneath the stack; no hard border.
- The card face carries a faint diagonal sheen: a lighter band near the avatars fading to warm grey, like a frosted acrylic tile. Back cards are flat white with lower shadow.
- Avatars have a 2–3 px white ring so the second avatar cuts cleanly into the first.

## 6. Components & patterns
- **Payment card:** amount, actor–verb–recipient line with inline verified badges (~18 px), memo with emoji, relative timestamp.
- **Avatar pair:** two ~56 px circles overlapping by ~30% (payer above payee).
- **Card stack:** three visible layers, top content-bearing, two blank-ish peeking backers that hint at "more".

## 7. Motion
Measured: 8 motion segments over 6.9 s, median **0.30 s** each (0.27–0.33 s), starting at 0.20, 1.03, 1.90, 2.77, 3.60, 4.47, 5.30, 6.17 s — a metronomic **~0.85 s** cadence with ~0.55 s holds. Motion fraction 0.35; `seamless_loop_likely: true`.
- Peaks mostly at 0.17–0.44 of each segment → ease-out / symmetric ease-in-out flicks; the last one (peak 0.75) is ease-in, setting up the loop seam.
- From frames (f1 at 1.15 s): the top card slides left and rotates about −4° while the next card rotates up from behind; content cross-fades with a light blur on the outgoing card (estimate). Sequence: $18.75 → $84 → $100 → $4,200 → repeat.

## 8. Brand system
n/a — not a brand system. Identity cues: X's blue verified badge, Chirp-like type, and the social grammar "A paid B" borrowed from Venmo-style feeds.

## 9. UX
- The stack conveys recency and volume without a list; good for a widget or lock-screen live activity.
- Weight-coded sentence makes who-paid-whom scannable in <1 s.
- Risks: grey secondary text fails AA; an auto-advance of 0.85 s is too fast to read a memo in production (fine as a demo). No visible affordance for swiping or pausing.

## 10. Craft signals
- Back cards rotated in opposite directions (≈+3°/−4°) so the pile never looks like a single drop shadow.
- Real curly quotes around memos, emoji inline at text size.
- Verified badges sit on the x-height midline, ~6 px after the name.
- Timestamp baseline aligned with the memo baseline, right edge at the same 40 px inset as the left padding.
- Identical segment lengths (0.30 s ± 0.03) show a single tokenised transition.

## 11. Reproduction recipe
```css
:root{--stage:#e4e4e6;--card:#f5f5f5;--ink:#111;--ink-2:#8c8c8c;--verified:#1d9bf0;--r-card:28px;
  --font:"Chirp","GT America","Inter",system-ui,sans-serif;}
body{background:var(--stage);font-family:var(--font)}
.stack{position:relative;width:665px;height:285px}
.card{position:absolute;inset:0;border-radius:var(--r-card);padding:40px;
  background:linear-gradient(120deg,#f7f7f7 0%,#fff 55%,#efecee 100%);
  box-shadow:0 24px 48px rgba(0,0,0,.06),0 2px 6px rgba(0,0,0,.04);
  transition:transform .3s cubic-bezier(.2,.8,.2,1),opacity .3s,filter .3s}
.card:nth-child(2){transform:translate(12px,40px) rotate(3deg);z-index:-1}
.card:nth-child(3){transform:translate(-8px,55px) rotate(-4deg);z-index:-2}
.card.leaving{transform:translateX(-40%) rotate(-4deg);opacity:0;filter:blur(4px)}
.amount{font:700 60px/1 var(--font);letter-spacing:-.02em;color:var(--ink)}
.who b{font-weight:700;color:var(--ink)} .who{font-size:26px;color:var(--ink-2)}
.avatars img{width:56px;height:56px;border-radius:50%;box-shadow:0 0 0 3px #fff}
.avatars img+img{margin-left:-18px}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm monochrome stage, crisp type, believable material. |
| Originality | 6 | Card-stack shuffle is a known pattern; the feed-as-stack framing is a nice touch. |
| Usability | 7 | Very scannable sentence structure; grey text and auto-advance speed hurt. |
| Craft | 8 | Consistent 0.3 s transitions, careful badge and quote details. |
