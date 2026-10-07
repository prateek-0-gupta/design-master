---
id: insp-1-51
source: inspora
category: Motion
status: analyzed
title: "Payment plans"
creator: "Praveen Kumar"
styles: [dark-premium, skeuomorphic, micro-interaction, aurora-glow]
patterns: [cartridge-slot-plan-selector, pricing-card, billing-toggle, feature-checklist-with-disabled-items, glow-ribbon-footer-badge, state-color-theming]
mode: dark
palette: ["#0d0d0f", "#19191b", "#2d2f32", "#207de1", "#308dee", "#f59a3a", "#ffffff", "#3a3b3e"]
type_families: ["Roboto (likely)"]
type_class: [neo-grotesk]
radius_px: [40, 32, 20, 9999]
motion: {durations_s: [0.7, 0.27, 0.23, 0.9], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 8, originality: 9, usability: 6, craft: 7}
craft_signals: [plan-color-floods-card-border-price-and-badge, cartridge-pins-and-dot-matrix-detail, unselected-cartridge-tilted-and-desaturated, disabled-features-ghosted-not-removed, outer-glow-under-badge-ribbon, slot-housing-flares-into-card-top]
anti_patterns: [ghosted-features-near-invisible, white-on-orange-badge-fails, mislabelled-billed-monthly-on-yearly, price-reads-as-ghost-before-selection]
---
# Payment plans — Praveen Kumar

## 1. Snapshot
- **Subject:** A 19.4 s, 3304×2160 capture of a Rive pricing widget. Two game-cartridge chips (blue = Monthly, orange = Yearly) float above a slot on a dark card, and inserting one selects the plan, recolouring price, border, toggle and a footer ribbon.
- **Why it's remarkable:** The plan choice becomes a physical act of plugging in a cartridge. The colour of the inserted part then floods the whole card, so state is legible at a glance.

## 2. Composition & layout
- **Card:** about 1280×690 px in the 2000-px key frame (≈2110×1140 real). It is split roughly 45/55: left is the toggle, price, "Billed Monthly" and the CTA; right is "Includes:" plus six checklist rows at about 77 px pitch.
- **Slot:** A trapezoid housing (≈280 px wide) rises from the card's top edge at x≈33%. The two cartridges hover above it, with the inactive one rotated about 15° and offset to the right.
- **Ribbon:** A footer ribbon (≈100 px tall) appears beneath the card only once a plan is inserted. It reads like a tray sliding out from under the card.
- **Bookends:** The first and last frames show the piece embedded in the Rive Marketplace page (sidebar with "Payment Plans", inputs list), with a slight blur on the intro.

## 3. Typography
- A single sans that looks like Roboto (double-storey "g", flat terminals on "y", Roboto-style "$"). Regular 400 throughout.
- **Price:** about 110 px real (≈68 px in the key frame), set as "$ 20.00" with a spaced dollar sign.
- **Other sizes (key-frame px):** "Includes:" about 40 px; feature rows about 32 px; CTA "Get Started" about 44 px; badge text about 34 px.
- There is no weight contrast; hierarchy is size and colour only.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #0d0d0f | stage | 69% |
| #19191b | card body | 8% |
| #2d2f32 | CTA, toggle well | 4% |
| #207de1 / #308dee | Monthly accent: border, price, ribbon, glow | ~10% |
| #f59a3a (approx) | Yearly accent | swaps with blue |
| #ffffff | text | 2% |
| #3a3b3e (approx) | ghosted features, price before insert | 1% |

WCAG checks:
- White on card is 17.56:1.
- Blue price #207de1 on #0d0d0f is 4.70:1 (pass); #308dee is 5.70:1.
- White text on the blue ribbon is 4.13:1 (large only).
- White on the orange ribbon (≈#f59a3a) is **2.20:1 (fail)**.
- Ghosted features (≈#3a3b3e on #19191b) are **1.57:1**, effectively invisible.

## 5. Depth & material
- **Cartridges:** Rendered objects with a metal shell, gold edge pins and an LED dot-matrix face (blue or orange) that glows when active, plus a coloured halo of about 40 px blur.
- **Card:** Two layers: an outer #19191b shell with about a 40 px radius, and an inner panel inset 18 px with a 2 px accent stroke and about a 32 px radius.
- **Ribbon:** A large soft outer glow (≈60 px, same hue) that makes the card look lit from beneath.
- **Housing:** The slot is a glossy dark trapezoid with a curved flare where it meets the card, which reads as moulded plastic.

## 6. Components & patterns
- **Cartridge-slot selector:** drag or click a cartridge to plug it in. The other cartridge pops out and tilts.
- **Segmented billing toggle:** a dot plus label inside a dark pill. The active side carries the coloured dot (cyan for Monthly, orange for Yearly).
- **Feature checklist:** rows not included in the plan stay in place but are ghosted, so the yearly upgrade "lights up" two extra rows.
- **CTA:** a #2d2f32 filled button about 540×130 px real, radius about 20.
- **Badge ribbon:** a check-circle icon plus a tagline per plan ("Best For Those Who Want To Try It Out" / "Best For Long-Term…").

## 7. Motion
Measured: 19.37 s at 60 fps, 8 short segments, motion fraction 0.16, median segment 0.27 s, not a seamless loop.
- **Opening (0.93–1.63 s, 0.70 s, peak 0.12 → ease-out):** The intro zoom from the marketplace page into the widget.
- **Mid-video swaps:** Repeated 0.20–0.27 s segments (2.67, 4.50, 5.97, 8.13, 12.27, 14.10 s) are cartridge swaps. Shapes mix ease-out (peak 0.31) and ease-in (peak 0.79–0.81), which fits an eject (fast start) followed by an insert that accelerates into the slot.
- **Closing (16.57–17.47 s, 0.90 s, ease-out):** The zoom back out to the page.
- **Colour transitions:** Across frames the price fills from ghost grey to accent, and the ribbon slides down. These are estimated at under 0.3 s and coincide with the measured segments.

## 8. Brand system
n/a — not a brand system. Identity cues: a retro-hardware (game cartridge / SIM) metaphor and a two-hue plan coding (electric blue vs amber) applied consistently to every accent surface.

## 9. UX
- **Strengths:** The selected plan is unmistakable, and the inclusion difference between plans is shown in place.
- **Risks:**
  - The interaction is novel, so users may not realise the cartridges are draggable.
  - Before a plan is inserted, the price is ghosted to near-invisible (frame 3.23 s), hiding the most important number.
  - "Billed Monthly" remains under the $200 yearly price, a copy bug.
  - The orange ribbon text fails contrast.
  - Ghosted features are unreadable rather than merely de-emphasised.

## 10. Craft signals
- One accent hue drives border, price, toggle dot, cartridge LEDs, ribbon and glow: six surfaces from one token.
- The inactive cartridge is tilted about 15° and dimmed, while the active one is upright and haloed.
- The inner panel inset (≈18 px) keeps a concentric radius with the outer shell.
- The cartridge has a gold pin row and a dot-matrix face, small physical details at about 3 px.
- Excluded features are kept as ghost rows so the card height never jumps between plans.

## 11. Reproduction recipe
```css
:root{--stage:#0d0d0f;--card:#19191b;--well:#2d2f32;--ink:#fff;--ghost:#3a3b3e;
  --accent:#207de1;--r-outer:40px;--r-inner:32px;}
.card[data-plan=yearly]{--accent:#f59a3a}
.card{background:var(--card);border-radius:var(--r-outer);padding:18px;position:relative}
.card .panel{border:2px solid var(--accent);border-radius:var(--r-inner);padding:32px;
  box-shadow:0 0 24px color-mix(in srgb,var(--accent) 45%,transparent);transition:border-color .25s,box-shadow .25s}
.price{font:400 68px/1 Roboto,sans-serif;color:var(--accent);transition:color .25s ease-out}
.card:not([data-plan]) .price{color:var(--ghost)}
.feature[aria-disabled=true]{opacity:.25}   /* raise to .45 for legibility */
.ribbon{background:var(--accent);border-radius:0 0 var(--r-outer) var(--r-outer);margin-top:-40px;padding:56px 24px 20px;
  box-shadow:0 20px 60px color-mix(in srgb,var(--accent) 60%,transparent);
  animation:tray .3s cubic-bezier(.2,.9,.3,1)}
@keyframes tray{from{transform:translateY(-100%)}}
.cartridge{transition:transform .27s cubic-bezier(.4,0,1,1)}
.cartridge[aria-pressed=false]{transform:translate(120px,-30px) rotate(15deg);filter:saturate(.4) brightness(.7)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Rich glow-on-black with tactile hardware props; the colour flood is satisfying. |
| Originality | 9 | Cartridge insertion as plan selection is a genuinely new pricing metaphor. |
| Usability | 6 | State is clear, but discoverability, ghost contrast and the copy bug hurt it. |
| Craft | 7 | Consistent accent token and concentric radii; the uniform 400 weight and label bug feel unfinished. |
