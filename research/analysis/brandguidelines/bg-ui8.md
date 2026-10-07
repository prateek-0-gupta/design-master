---
id: bg-ui8
source: brandguidelines
category: marketplace
status: analyzed
title: "UI8 — The Ultimate Marketplace for Designers (homepage)"
creator: "UI8 (Robot Global FZCO)"
styles: [dark-premium, photo-led, bento-grid]
patterns: [featured-trending-recent-segmented-control, product-card-grid-with-price-chip, category-tile-grid, author-spotlight-carousel, trusted-by-logo-row, newsletter-capture-gradient-border, all-access-pass-upsell]
mode: dark
palette: ["#141414", "#1c1c1c", "#2d2d2d", "#f5f5f5", "#9aa3ab", "#2d68ff", "#00b27a"]
type_families: ["CircularXX (census, 400/450/500)"]
type_class: [geometric-sans]
radius_px: [16, 22, 12, 99]
motion: {durations_s: [0.2, 0.3, 0.35, 0.4, 0.55], easing: [ease, "cubic-bezier(0.215,0.61,0.355,1)", "cubic-bezier(0.34,1.56,0.64,1)"], loop: false}
scores: {aesthetics: 6, originality: 4, usability: 7, craft: 6}
craft_signals: [inner-top-highlight-1px, consistent-tracking-minus-0-02em, three-step-radius-scale, css-transition-token-set, gradient-border-input]
anti_patterns: [muted-meta-text-below-aa, mobile-capture-blocked-by-challenge, template-grid-repetition]
---
# UI8 — The Ultimate Marketplace for Designers — UI8 (Robot Global FZCO)

## 1. Snapshot
- **Subject:** The UI8 homepage (`ui8.net/?rel=1042`), a marketplace for design kits, templates, illustrations and fonts. The capture is the live desktop home (no redirect, no Wayback). The census title is "UI8 | The Ultimate Marketplace for Designers". The mobile capture is a Cloudflare "Performing security verification" page, not the design (see §9).
- **Why it's remarkable:** It sells a large catalogue (the headline states 14,617 resources) with almost no decoration. Product thumbnails carry the colour, and a single blue accent drives every action.

## 2. Composition & layout
- **Hero:** centred, roughly 56–64 px type, sitting on a dark field with faint translucent tiles behind it. Header at y≈36, with the logo at x≈56 and the cart icon at x≈1368.
- **Segmented control:** "Featured | Trending | Recent" in a pill, centred at y≈512.
- **Product grid:** a 4-up grid. Cards are about 314 px wide with a 24 px gap (x 56 to 1384), each with a 16 px radius thumbnail and a title, creator and price beneath.
- **Category grid:** a 3-up set of 6 px-radius image tiles (about 373 px wide), each with a title and a format line.
- **Author spotlight:** a rounded box (about 960 px wide) with three preview images and a follow button.
- **Footer:** a four-column link set (Browse, Platform, Connect) and a legal row.
- **Mobile:** not captured usefully (see §9).

## 3. Typography
- **Family:** CircularXX only (loaded at 400, 450 and 500). The census shows 242 uses of the same stack, so the page runs on a single family.
- **Scale (census):** 13 px (82 uses), 15 px (55), 16 px (50), 14 px (24), 20 px (4), 22 px (3), 34 px (2), 48 px (1), 64 px (3). The 64 px step is the hero, and body text sits at 13–16 px.
- **Weights:** 450 (133 uses) is the dominant text weight, with 400 (73), 500 (32) and 700 (4). The in-between 450 weight is the tell that the family was tuned for dark UI.
- **Tracking:** `-0.28px` on 217 nodes, which is about -0.02em at 14 px. It is applied at a single px value across nearly all text, and only the labels use positive tracking (0.475 px and 0.55 px at 9.5 px and 11 px).
- **Line heights:** 14 px (82 uses) for 13 px text, 20 px (55) for 15 px, and 24 px for 16 px.

## 4. Colour
| Hex | Role | Approx share (tile 1) |
|---|---|---|
| #121212 | page background | ~50% |
| #25262a | card and panel fill | ~15% |
| #f9f9f6 | headline white | ~5% |
| #9aa3ab | secondary text (census `--text-dim`) | small |
| #adb7be | body text (census, 107 uses) | small |
| #2d68ff | accent: buttons, Follow, price highlights | small |
| #00b27a | status green (`--green`) | very small |

- **WCAG pairs (contrast.py):** #f5f5f5 on #141414 **16.9:1**. #adb7be on #141414 **9.03:1**. #9aa3ab on #141414 **7.19:1**. #ffffff on #2d68ff **4.63:1** (passes AA-normal, barely). #5a6068 on #202020 **2.57:1**, which fails. #5c5c5c (92,92,92 at 16 uses) is also very low on the dark field.
- The census token `--text-muted` (#5a6068) is the failing role. It is used for meta text, so the labels under titles are hard to read.

## 5. Depth & material
- The dominant depth device is an inner top highlight. The census shows `rgba(0,0,0,.25) 0 6px 12px` combined with `rgba(255,255,255,.08) 0 1px 1px inset` on 72 nodes, which lifts each control off the field.
- Three surface steps (#141414, #1c1c1c, #202020, #282828) give layering without strong shadows.
- Thumbnails are the only large sources of colour; the UI itself is near-monochrome.

## 6. Components & patterns
- **Segmented control:** a pill with a gradient-edged active state.
- **Product card:** 16 px radius thumbnail, 16 px inner padding, title on one line with ellipsis, creator avatar + category chip, price right-aligned.
- **Price chip:** the price sits on the card's title row ("$129", "from $129" for All-Access).
- **Category tile:** full-bleed illustration tile with a format line (for example "Figma, Sketch").
- **Newsletter field:** a pill input with a blue-to-violet gradient stroke and an animated icon at the right.
- **Trust row:** a faded logo marquee under "TRUSTED BY" (Amazon, Google, Microsoft, Netflix, PayPal, Shopify, Spotify, Stripe).
- **All Access upsell:** a "30% OFF" pill in the top navigation.

## 7. Motion
- Measured from the census CSS transitions, not from video.
- **Durations (s):** 0.2 (color, background, opacity: 100+ uses), 0.3 (opacity), 0.35 (opacity with `cubic-bezier(0.215,0.61,0.355,1)`), 0.4 (transform), 0.55 (transform with `cubic-bezier(0.34,1.45,0.5,1)`).
- **Easings:** `ease` for most colour changes. `cubic-bezier(0.215,0.61,0.355,1)` is an ease-out (decelerating). `cubic-bezier(0.34,1.56,0.64,1)` overshoots (peak above 1), used on two transform transitions for a small spring.
- No looping animation was observed. The hero background tiles are static in the capture.

## 8. Brand system
n/a — not a brand system. This is a marketplace homepage. Identity cues: the blue dot in the logo mark (`#2d68ff`), the dark UI, and a single rounded-square mark. The brand's visible system is the product thumbnails.

## 9. UX
- Clear primary paths: sign up, browse, and a "30% OFF" All-Access pill in the header.
- Filtering is limited to Featured, Trending and Recent. Categories are a separate row below the fold, so the homepage has no inline filters.
- **Capture failure:** the mobile 390 px sheet is a Cloudflare challenge ("Performing security verification", "Verify you are human"). The mobile design is therefore not analysed and nothing is claimed about it. The desktop capture is valid.
- Weak spots: meta text in #5a6068 is below AA, and the homepage is long (scroll height 5,229 px in the census) with three similar product grids.

## 10. Craft signals
- One tracking value (`-0.28px`) carries almost every text node, so line-length and optical density stay consistent across sizes.
- Radii step through 8, 10, 12, 16, 18, 22 px, with `99px` for pills and `50%` for avatars.
- Inner top highlights on every control.
- The transitions form a small token set (0.2 s colour; 0.35 s ease-out opacity; 0.3 s overshoot transforms).

## 11. Reproduction recipe
```css
:root{
  --bg:#141414; --surface:#1c1c1c; --surface-2:#202020; --elev:#282828;
  --text:#f5f5f5; --text-dim:#9aa3ab; --body:#adb7be; --accent:#2d68ff; --green:#00b27a;
  --r-ctrl:12px; --r-card:16px; --r-panel:22px; --r-pill:99px;
  --track:-.28px;
  --ease-out:cubic-bezier(.215,.61,.355,1);
  --ease-spring:cubic-bezier(.34,1.56,.64,1);
}
body{background:var(--bg);color:var(--body);font:450 15px/20px CircularXX,sans-serif;letter-spacing:var(--track);}
.btn{background:var(--accent);color:#fff;border-radius:var(--r-pill);box-shadow:0 6px 12px rgba(0,0,0,.25),inset 0 1px 1px rgba(255,255,255,.08);transition:background .2s ease,color .2s ease;}
.card{background:var(--surface);border-radius:var(--r-card);transition:transform .4s var(--ease-out);}
.card:hover{transform:translateY(-2px);}
.meta{color:#8a929a;font-size:13px;line-height:14px;} /* do not use #5a6068 for text */
h1{font:500 64px/64px CircularXX,sans-serif;letter-spacing:var(--track);}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Calm dark field with clean product thumbnails, but the page is a standard marketplace grid. |
| Originality | 4 | A dark marketplace grid with a segmented control and price chips is a familiar template pattern. |
| Usability | 7 | Clear browse paths and sign-in; meta text is low contrast and there are no inline filters. |
| Craft | 6 | Consistent tracking and tokenised surfaces, but several meta tints fail contrast. |
