---
id: bg-framer-wesite-builder
source: brandguidelines
category: promoted-landing
status: analyzed
title: "Framer: AI design agent (homepage)"
creator: "Framer"
styles: [dark-premium, bento-grid, photo-led]
patterns: [dark-canvas-hero-with-glow-video, logo-wall-social-proof, bento-feature-grid, product-screenshot-cards, shipped-sites-masonry, community-feed-mockup, prompt-box-cta, footer-link-matrix]
mode: dark
palette: ["#000000", "#111111", "#ffffff", "#999999", "#0099ff", "#00bb88"]
type_families: ["GT Walsheim Medium (headings, census)", "Inter (body, census)", "Input Mono (labels, census)"]
type_class: [neo-grotesk, mono]
radius_px: [8, 15, 20, 100]
motion: null
scores: {aesthetics: 8, originality: 5, usability: 7, craft: 8}
craft_signals: [single-black-canvas-section-rhythm, glow-hero-video-frame, stepped-display-tracking, full-bleed-product-mock-cards, mono-label-system, pill-cta-pairing, footer-link-matrix]
anti_patterns: [dim-grey-captions-below-aa, low-contrast-card-captions, very-long-single-page]
---
# Framer: AI design agent (homepage) — Framer

## 1. Snapshot
- **Subject:** Framer's own marketing homepage, reached through the referral link `framer.link/lee72`. The link redirects to `framer.com/?via=lee72` with a tracking id appended, so the capture is Framer's live home, not a template. Title on capture: "Framer: AI design agent". No subpages were captured.
- **Why it's remarkable:** A product homepage that is almost entirely black and still reads as one system. The product UI is the imagery. A glowing hero video, bento cards with real screenshots and a prompt box that doubles as a live example carry the page.

## 2. Composition & layout
- **Desktop grid:** 1440 px wide with a 120 px side margin, so content runs x≈120 to x≈1320 (a 1200 px column). The header sits at y≈32 with the wordmark at x=120 and the "Sign up" pill ending at x≈1320.
- **Hero:** the H1 is about 54 px, two lines with a line pitch of about 55 px, and sits at y≈170 to y≈270. The rounded video frame spans the full 1200 px column and is about 672 px tall (y≈372 to y≈1044), with a 0:36 badge in its lower right.
- **Logo wall:** eight logos in a 4 × 2 grid, centred.
- **Feature section:** a bento of wide and narrow cards. The "Agents" panel is a narrow right column (about 260 px) beside a wide preview card. Corners are 15 px and 20 px, with a 1 px white ring at 10% opacity.
- **Mobile (390 px):** the bento collapses to one column with about 20 px side gutters. The logo row runs off the right edge and is clipped mid-logo ("DOOR"), so it scrolls horizontally.

## 3. Typography
- **Families (census):** headings render as GT Walsheim Medium (9 uses). Body copy is Inter (238 uses, plus 170 for "Inter Variable"). Labels and code-like chips use Input Mono (18 Regular and 6 Bold uses). JetBrains Mono appears once.
- **Scale (census):** 12 px (172 uses), 14 px (114), 13 px (83), 18 px (28), 44 px (5), 54 px (4). Body sizes cluster at 12–14 px and the display sizes stop at 54 px.
- **Line heights (census):** 19.6 px (104 uses), 14.4 px (83), 20.8 px (45). The 48.4 px value pairs with the 44 px display size (1.1).
- **Tracking:** body text is `-0.1px` (112 uses). Display sizes step down: `-0.2px` (33), `-0.6px` (11), `-1.76px` (5) and `-2.16px` (4). The two display values are both about -0.04em at 44 px and 54 px respectively, so the headline tightens as it grows.
- **Weights:** 500 (211 uses) carries nav and card titles, with 400 (190), 600 (36) and 700 (10).

## 4. Colour
| Hex | Role | Approx share (desktop tiles) |
|---|---|---|
| #000000 | page canvas | 70–90% of each tile |
| #111111 | raised panels, feature frames | 7–22% |
| #ffffff | headlines, primary CTA fill | 1–5% |
| #999999 | secondary text (census, 126 uses) | text only |
| #0099ff | accent: CWV values, analytics series | small |
| #00bb88 | "good" status badge | small |

- **WCAG pairs (contrast.py):** #ffffff on #000000 **21.0:1**. #999999 on #000000 **7.37:1**. #00bb88 on #000000 **8.46:1**. #0099ff on #000000 **7.0:1**.
- **Failing pair:** #666666 on #000000 is **3.66:1** (fails AA-normal). It is used on the dimmest captions under the cards.
- The CSS tokens include `#cbff00`, but no sampled pixel shows it, so it is not counted.

## 5. Depth & material
- Depth comes from light, not shadow. The hero has a blue radial glow behind a black browser frame. Dominant tile colours include `#010221` and `#181e5f`.
- Feature cards are separated by hairline strokes and a 1 px inner highlight. The census lists a handful of shadow values: `0 2px 6px rgba(0,0,0,.2)` (6 uses) for small elements, and a few large ambient ones (`0 26–40 px 42–64 px`, one use each) for floating panels.
- Product frames sit inside macOS-style windows with three 6 px traffic-light dots.

## 6. Components & patterns
- **Pill CTA pair:** "Get started for free" (white fill, black text) next to "Download app" (dark grey fill with a download glyph). Both are about 34 px tall with fully rounded ends.
- **Bento cards:** a screenshot, a 20–24 px title and a one-line description, with an arrow link ("Start with Agents") bottom-left.
- **Logo wall:** monochrome white logos (Dribbble, LEGORA, Zapier, Perplexity, Cal.com, Mixpanel, Miro, DoorDash), sized by visual weight rather than a fixed box.
- **Shipped-sites masonry:** a mixed grid of phone and desktop frames. Some tiles carry duration badges such as "01m 49s", which marks embedded video.
- **Community feed mockup:** a screenshot of Framer's community feed with a "Trending Templates" list. It shows the product rather than describing it.
- **Prompt box:** a rounded input with a model selector ("GPT 6 Sol") and four suggestion chips.
- **Footer:** six link columns (Product, Marketplace, Resources, Solutions, Compare, Company), with sub-groups such as Business and By Framer.

## 7. Motion
- Not measurable from these captures. The hero is an embedded video and the census has no CSS transition values (`transition` is empty), so no timings are stated.

## 8. Brand system
n/a — not a brand system. This is a product homepage. Identity cues: a black canvas, a white wordmark and a blue hero glow. The brand's approach is "the product is the picture", with almost no decorative graphics.

## 9. UX
- The hero offers two equal CTAs (sign-up and download) and a "Start without AI" text link under the prompt box, which keeps the path to conversion short.
- The prompt box is a live example of the product, with four starter chips ("Create personal portfolio", "Build startup site", "Launch landing page", "Start company blog").
- Weaknesses: the captions under the bento cards are dim grey on black at small sizes, which hurts reading. The page is long (scroll height 10,741 px in the census) and carries several social-proof blocks (logo wall, shipped sites, trusted-by stories, community) before the final CTA.

## 10. Craft signals
- Display tracking is stepped by size (-0.2, -0.6, -1.76 and -2.16 px) rather than set once.
- One mono family (Input Mono) is used for the product-UI labels, which keeps the screenshots and the page chrome in one voice.
- The desktop column is a fixed 1200 px inside a 1440 px viewport, and the mobile layout uses a single column.
- The footer uses equal heading-then-link stacks with matched column starts.

## 11. Reproduction recipe
```css
:root{
  --canvas:#000; --panel:#111; --ink:#fff; --ink-2:#999; --accent:#09f; --ok:#0b8;
  --radius-chip:8px; --radius-card:20px; --radius-pill:100px;
  --font-head:"GT Walsheim Medium","Inter",sans-serif;
  --font-body:"Inter",sans-serif;
  --font-mono:"Input Mono","JetBrains Mono",monospace;
}
body{background:var(--canvas);color:var(--ink);font:400 14px/19.6px var(--font-body);letter-spacing:-.1px;}
h1{font:500 54px/55px var(--font-head);letter-spacing:-2.16px;}
h2{font:500 44px/48.4px var(--font-head);letter-spacing:-1.76px;}
.caption{color:var(--ink-2);font-size:13px;line-height:20.8px;}
.chip{background:var(--panel);border-radius:var(--radius-chip);font:500 12px/14.4px var(--font-mono);padding:6px 10px;}
.pill{border-radius:var(--radius-pill);height:34px;padding:0 16px;background:#fff;color:#000;}
.card{background:var(--panel);border-radius:var(--radius-card);box-shadow:0 0 0 1px rgba(255,255,255,.1);}
.hero-glow{background:radial-gradient(60% 60% at 50% 40%,#181e5f 0%,#000 70%);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Black canvas, one headline style and product-led imagery make a cohesive, premium look. |
| Originality | 5 | The dark-premium SaaS homepage with a glowing hero and bento cards is now a common pattern. |
| Usability | 7 | Clear CTAs and a live prompt example; dim captions and a very long page cost points. |
| Craft | 8 | Stepped display tracking, one mono label family and a tidy footer matrix. |
