---
id: insp-mega-menu
source: inspora
category: Web
status: analyzed
title: "Mega Menu Animation"
creator: "@gabriell_lab"
styles: [glassmorphism, photo-led, luxury, cinematic-3d]
patterns: [frosted-mega-menu, two-column-product-list, coming-soon-mono-badge, hover-row-highlight, promo-image-tile-in-menu, pill-nav-active-chip, two-tone-headline, glass-email-capture]
mode: mixed
palette: ["#d6d7d2", "#92968b", "#4f3e2a", "#3e3123", "#795933", "#8c6f47", "#25201a", "#b6b3aa"]
type_families: ["Neue Montreal / Geist-style neo-grotesk (likely)", "Geist Mono / IBM Plex Mono (badges, likely)"]
type_class: [neo-grotesk, mono]
radius_px: [24, 16, 9999, 6]
motion: {durations_s: [0.37, 0.13], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 6, usability: 7, craft: 8}
craft_signals: [two-tone-headline-by-value-not-hue, mono-caps-badges-for-status, 3d-monochrome-product-icons, hover-tile-lighter-not-outlined, sunset-promo-tile-echoes-hero-palette, active-nav-chip-matches-menu-glass]
anti_patterns: [menu-description-grey-below-aa, nav-on-light-sky-low-contrast, promo-text-cropped]
---
# Mega Menu Animation — @gabriell_lab

## 1. Snapshot
- **Subject:** A 2560×1920, 6.2 s seamless loop of a fintech hero for "Grain" (stablecoin payments). Hovering "Products +" drops a frosted-glass mega menu of six products plus a sunset promo tile over a heavily blurred golden-hill landscape.
- **Why it's remarkable:** It is a restrained, expensive-feeling menu. Warm-grey frosted glass, 3D monochrome product icons and mono "COMING SOON" badges sit over an out-of-focus cinematic photo, and the only saturated colour is the promo tile's sunset.

## 2. Composition & layout
CSS px are about half of the 2560 capture.
- **Nav:** "Grain™" wordmark at x≈80, ~40 px. The links (Products +, Resources +, Compliance) are centred at ~18 px. The active "Products" sits in a translucent pill chip (radius 9999).
- **Mega menu:** ~1180×385 CSS px, starting ~45 px below the nav, left edge at x≈375 and bleeding off the right in the capture.
  - A **2×3 product grid** with ~440 px columns. Each item has a 26 px icon, a title at ~17 px and three description lines at ~15 px.
  - A **~280 px promo column** with a sunset photo and "Read our Blogpost ↗" plus a 3-line teaser.
- **Hero copy:** bottom-left, "Built for Modern Payments" (~52 px) with a 2-line sub (~28 px). A glass email field ("What's you work mail?") is at bottom-right.

## 3. Typography
- **Primary face:** a neo-grotesk with a single-storey "a" in the wordmark and open apertures, close to Neue Montreal or Geist.
  - Headline: Regular 400, tracking about −0.02 em.
  - Menu titles: Medium 500.
  - Descriptions: Regular, about 1.45 leading.
- **Two-tone headline:** "Built for" in white, "Modern Payments" in a warm beige (~#c9bfae). The value shift replaces a weight change.
- **Mono badges:** "COMING SOON" in ~12 px uppercase mono with +0.06 em tracking, in a 1 px-bordered rounded box (radius ~6 px).
- **Typos:** "What´s you work mail?" uses an acute accent instead of an apostrophe and a "you" typo; "Virtual Accounts" reuses the Invoicing description. These are copy QA misses.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #d6d7d2 | frosted menu surface (light, warm grey) | 14% |
| #92968b / #b6b3aa | misty sky, upper hero | 19% |
| #4f3e2a / #3e3123 / #25201a | dark earth tones, lower hero | 33% |
| #795933 / #8c6f47 / #614b31 | golden hill light | 17% |
| #1e1e1e (est.) | menu titles | — |
| ~#6a6a66 (est.) | menu descriptions | — |

WCAG checks:
- Menu titles on glass are **11.52:1**.
- Descriptions (~#6a6a66 on #d6d7d2) are **3.75:1**, which fails AA for 15 px.
- "COMING SOON" (~#8a8a86) is **2.39:1**.
- Nav white on the misty sky (#92968b) is **3.02:1**, a borderline large-only pass.
- Hero white on #4f3e2a is **10.22:1**, and beige "Modern Payments" is **5.62:1**.

## 5. Depth & material
- **Menu panel:** a frosted glass with about 85% opaque warm-grey fill, a heavy backdrop blur (the hero is already blurred), radius ~24 px, a 1 px lighter top edge and a soft drop shadow.
- **Hover state:** The hovered item gets a lighter inner tile (~#e6e6e1, radius ~16 px) with no border, a surface lift (seen moving from Stablecoin Checkout to Virtual Accounts at 1.73 s and 3.12 s).
- **Icons:** small 3D-rendered monochrome objects (folded plates, a knob, a pin, a flag) in matte graphite, which carry the "physical product" feel.
- **Background:** The photo itself is a motion-blurred landscape, essentially a gradient with texture.

## 6. Components & patterns
- **Mega menu:** icon plus title, an optional status badge and a description, in two columns, with a featured-content rail on the right.
- **Status badges:** mono caps in an outlined chip, for "COMING SOON".
- **Active nav item:** a glass pill.
- **Email capture:** a dark glass pill (~#3a3a36 at 70%) with placeholder text, sitting low-right with no visible button.

## 7. Motion
- **Measured:** 6.23 s at 30 fps, motion_fraction **0.08**, 2 segments; **seamless_loop_likely = true** (first/last diff 0.18).
  - **0.37–0.73 s (0.37 s, ease-out, peak 0.32):** the menu opens (fade plus a slight drop or scale from the nav).
  - **4.37–4.50 s (0.13 s, ease-in-out):** the menu closes, faster than it opens, which is correct asymmetry.
- **Between:** from ~1 to 4 s the hover highlight moves between rows (below threshold; frames show Stablecoin → none → Virtual Accounts). Background photo motion is negligible.
- **Timing:** The 0.37 s open and 0.13 s close are a good pair to copy.

## 8. Brand system
n/a — not a brand system. Identity cues:
- the "Grain™" wordmark;
- an earthy, cinematic palette (wheat, soil, mist) that suits the name;
- 3D graphite product icons;
- mono status labels.

## 9. UX
- **Strengths:** Rich but scannable menu with a clear icon/title/description hierarchy; status badges set expectations; the promo slot drives content.
- **Issues:**
  - Description text fails AA.
  - Duplicate copy (Virtual Accounts = Invoicing).
  - Typo in the email placeholder.
  - The email field has no submit button or label.
  - The nav's white text on pale mist is borderline.

## 10. Craft signals
- The open duration (0.37 s ease-out) is roughly 3× the close duration (0.13 s), a deliberate asymmetry.
- The hover row is a lighter filled tile with a ~16 px radius nested in a ~24 px panel radius, so the inner radius is smaller than the outer one, a correct nesting.
- Icons are one consistent 3D graphite material set.
- The sunset in the promo tile echoes the hero's gold, so the menu's only colour is on-palette.
- The headline is two-toned via value (white/beige) at a single weight.
- The active nav chip uses the same frosted material as the menu, linking trigger and panel.

## 11. Reproduction recipe
```css
:root{--glass:rgba(222,223,217,.86);--glass-hover:#e8e8e3;--ink:#1e1e1e;--muted:#55554f;/* darkened for AA */
  --beige:#c9bfae;--r-panel:24px;--r-item:16px;--font:"Neue Montreal","Geist",system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,monospace}
.nav a[aria-expanded=true]{background:rgba(255,255,255,.18);backdrop-filter:blur(12px);border-radius:9999px;padding:6px 14px}
.mega{position:absolute;top:calc(100% + 16px);display:grid;grid-template-columns:1fr 1fr 280px;gap:8px;padding:12px;
  background:var(--glass);backdrop-filter:blur(30px) saturate(1.1);border-radius:var(--r-panel);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 30px 60px rgba(30,20,10,.25);
  opacity:0;transform:translateY(-8px) scale(.98);transform-origin:top center;
  transition:opacity .13s ease-in-out,transform .13s ease-in-out}
.mega.open{opacity:1;transform:none;transition:opacity .37s cubic-bezier(.16,1,.3,1),transform .37s cubic-bezier(.16,1,.3,1)}
.item{display:grid;grid-template-columns:26px 1fr;gap:12px;padding:14px;border-radius:var(--r-item);transition:background .15s}
.item:hover{background:var(--glass-hover)}
.item h4{font:500 17px var(--font);color:var(--ink)}.item p{font:400 15px/1.45 var(--font);color:var(--muted)}
.badge{font:400 12px var(--mono);letter-spacing:.06em;text-transform:uppercase;border:1px solid #0000001f;border-radius:6px;padding:1px 6px}
h1 span{color:var(--beige)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A warm, cinematic, quiet-luxury palette with impeccable glass. |
| Originality | 6 | A well-known frosted mega-menu pattern, elevated by art direction rather than a new idea. |
| Usability | 7 | Clear structure and good timing; grey descriptions fail AA, and there is a copy duplication. |
| Craft | 8 | Nested radii, asymmetric timing and an icon set are excellent; text QA slips. |
