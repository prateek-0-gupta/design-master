---
id: bg-klarna
source: brandguidelines
category: guideline
status: analyzed
title: "Klarna Brand Guidelines"
creator: "Klarna (in-house)"
styles: [maximalist-color, photo-led, kinetic-type, playful-rounded, editorial-serif]
patterns: [full-bleed-photo-hero, oversized-condensed-headline, pink-and-ink-two-colour-core, scroll-reveal-sections, audio-version-button, sticky-section-subnav, inline-image-in-headline, brand-tone-manifesto-on-colour-field, phone-mockup-story-cards]
mode: mixed
palette: ["#ffa8cd", "#0b051d", "#f9f8f5", "#ffffff", "#efeff6", "#2d2344", "#d9ff8b", "#605f63"]
type_families: ["KlarnaTitle (Bold 700, condensed grotesk, custom)", "KlarnaText (Regular 400, Medium 500, custom)"]
type_class: [condensed, grotesk, display]
radius_px: [8, 20, 78, 100, 105]
motion: {durations_s: [0.2, 0.3, 0.4, 0.5, 0.56, 0.6, 0.8], easing: ["cubic-bezier(0.25,0.46,0.45,0.94)", "cubic-bezier(0.19,1,0.22,1)"], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [type-as-hero-208-to-320px, negative-tracking-1pct-on-display, ink-not-black-0b051d, pink-chip-lockup-for-co-brand, audio-version-of-guidelines, two-easing-curves-quad-and-expo-out, sticky-subnav-with-arrow-active, copy-set-in-brand-voice]
anti_patterns: [scroll-reveal-sections-blank-in-static-capture, white-on-pink-fails, 20190px-single-page, headline-line-height-below-1]
---
# Klarna Brand Guidelines — Klarna

## 1. Snapshot
- **Subject:** brand.klarna.com, a live scroll site. `site_meta.json`: requested the root, final URL `/our-brand#straight-up` (the second page, with an in-page anchor). Captured: Home (20,190 px tall) and "Our brand" (7,831 px). Much of the screenshot is blank white or cream. Those sections are scroll-triggered reveals (the CSS has 0.8 s / 0.56 s `transform, opacity` transitions) and had not triggered when the tile was shot. The mobile strips confirm the content exists (ice-cream hand, cards, headphone phone). All descriptions come from tiles that did render: hero (t01), t08, t10, t12 on home and sub t01-t02.
- **Why it's remarkable:** the brand is expressed by a cat under a pink curtain, then a 208-320 px condensed headline in a blue-black ink, then manifesto text set directly on a pink field in the brand's own voice. It is a quirky voice enforced by large type.

## 2. Composition & layout
- **Header (1440 px):** white "Klarna" logo at x=40,y=73 (about 107×28 px), a pink pill menu button (64×40 px, #ffa8cd, 20 px radius) at x=162, "Play audio version" pill (226×40 px, white, 20 px radius) at x=1120 and a 40 px circle search button at x=1360.
- **Hero:** 900 px high full-bleed photograph of a grey-and-white cat under a pale pink curtain, on a mustard carpet. The title "Brand guidelines" is white, KlarnaTitle Bold at about 80 px, left at x=40,y=750-820, with a "SCROLL TO EXPLORE" 12 px caps caption below.
- **Home flow:** alternating full-bleed bands: cream #f9f8f4 and ink #0b061d (each about 800-1580 px tall), then a white band with mock-ups. Statement H1 "Refreshingly different", "Brilliantly out of the ordinary" and "Making everyday money moments better all round" appear as 208-320 px lines of KlarnaTitle (line-height 0.85).
- **Gallery band (t08):** a 690×750 px billboard photo (pink "Kl..." with ice cream) at x=20, with a 690×250 px ("Pick pink") and two 335×495 px photos at x=730 and x=1085. Radius 8-20 px. Gutter 20 px.
- **Story-card band (t10):** a row of phone-shaped cards 291×630 px (78 px radius, hence the 78 px value in the radius census) on white: pink Apple, grey Rimowa with a faded brand list behind, ink Nike, cream Converse with a lime arch (#d9ff8b), cream "Klarna your..." card.
- **Our brand page:** a 140 px blank header zone, then H1 "Our brand" at 145 px (x=40, baseline y=745) with an audio pill (226×50 px, #efefef) beside it. A left sub-nav at x=40 (Our brand, Brand personality, Creative principles, Offbeat optimists, Strikingly relevant, Straight up; 14 px, active item with a "→"), content at x=270 to x=1400 (1130 px). Statement 36 px bold. H2 "Our brand personality" 95 px. An ink panel (1130 px wide, 20 px radius at top-right) shows "Curiously Bold" tiled in pink 145 px type. Then a full-bleed pink field with the manifesto at about 80 px.
- **Mobile 390 px:** hero photo with the title at 52 px; headlines at about 36-40 px with inline image chips ("Not for the sake of it, [balloon image] but to transform [pink car] the status quo"); cards one per column at 358 px wide.

## 3. Typography
Two custom faces: KlarnaTitle (Bold 700, condensed) and KlarnaText (400/500).

| Role | Spec |
|---|---|
| Mega statement | KlarnaTitle 700, 208 px / 176.8 px (0.85), tracking -2.08 px (-1%) |
| Extra mega | 240 px / 240 px; 320 px / 272 px |
| Page H1 | KlarnaTitle 145 px / 145 px; 95 px / 95 px |
| Hero H1 / manifesto | KlarnaTitle 80 px / 80 px, tracking -0.16 px (and 80/68 px) |
| Statement | KlarnaTitle 36 px / 36 px; 48 px / 57.6 px |
| Lead | KlarnaText 400, 24 px / 26.4 px, -0.24 px (-1%) |
| Body | KlarnaText 20 px / 28 px, -0.2 px; 14 px / 26.6 px or 18.9 px |
| Label | KlarnaText 500, 16 px / 17.6 px, -0.16 px |
| Caps caption | KlarnaText 400, 12 px, +0.36 px (3%) |

Tracking rule: -1% on display and lead sizes, 0 on small body, +3% on 12 px caps. Line-height drops below 1 (0.85) at mega sizes, which makes stacked lines touch descenders.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #ffa8cd | "Klarna pink", hero field, chips, logo ground | 15-56% of pink tiles |
| #0b051d | ink (called black in the CSS, rgb 11,5,29), text, dark bands | 12-87% of dark tiles |
| #f9f8f5 | cream ground | 55-100% of cream tiles |
| #ffffff | white ground | 50-100% |
| #efeff6 | light lavender panel | |
| #2d2344 | dark purple card (Nike story card) | |
| #d9ff8b | lime arch accent (Converse card) | accent |
| #605f63 | secondary text | |

The palette is two-colour (pink and ink) plus cream and white grounds; extra hues (lime, lavender, purple, red) occur only in photography and cards.

WCAG (contrast.py): ink #0b051d on pink **11.14:1**; ink on white **19.93:1**; ink on cream **18.77:1**; #605f63 on white **6.34:1** (on #efefef **5.51:1**). White on pink is only **1.79:1**, so the logo-on-pink is always ink and the white "Klarna" over the photo is a graphic, not text.

## 5. Depth & material
No shadows in the census. Radius is 8 px (small cards), 20 px (panels, pills), 78 px (phone cards), 100-105 px (circles). Depth comes from photography: glossy phones, pale chiffon, vinyl record, cards in the sky. The ink panel and the pink field are flat.

## 6. Components & patterns
- Pill buttons: menu (pink), audio (white or grey), search (circle).
- Sub-nav (sticky) with arrow marking the active item.
- Pink-chip "Klarna" lockup (pink rounded rect with ink wordmark) next to partner logos with a vertical hairline.
- Inline photo chips inside headlines (mobile and desktop).
- Billboard and phone mock-ups for application examples.
- Typographic repeated-line panel ("Curiously Bold" ×6).
- Manifesto on a flat pink field: "Hej. Klarna here. ... Because being different pays."

## 7. Motion
Real values from CSS: colour transitions 0.2-0.5 s `cubic-bezier(.25,.46,.45,.94)` (ease-out quad); reveals `transform 0.8 s` + `opacity 0.56 s` with `cubic-bezier(.19,1,.22,1)` (expo-out) and the quad curve for opacity; hover transforms 0.4 s expo-out; a 0.6 s expo-out transition on background-color. Combined with scroll triggers this explains the blank tiles. There is an audio version of the guidelines.

## 8. Brand system
- **Sections (home):** Our brand, How we speak, How we look (three H3 cards under "Explore our brand guidelines"). Our brand sub-sections: Brand personality, Creative principles, Offbeat optimists, Strikingly relevant, Straight up, then "See our creative principles at work" with Typography, Art direction and Voice.
- **Vision:** "To be the new standard for how people shop and pay."
- **Personality:** "Curiously Bold", the "Klarna spirit". Creative principles are three: Offbeat optimists (a surprising twist on the ordinary, "our own slightly Swedish way"), Strikingly relevant, Straight up.
- **Logo:** a rounded bold geometric wordmark shown in ink on pink at 1440×390 px; the "K" has a tall stem and a diagonal leg. Used white over photos, ink on pink, as a pink chip with a partner's logo.
- **Voice:** "Hej." greetings, short declaratives, punchy contrasts ("Because being different pays."), pink-cake metaphors.
- **Imagery:** surreal, tactile still lifes and hands with colourful nails and rings, pastel skies, glossy objects, always with a pink or blue note.
- **Token decisions worth stealing:** ink #0b051d instead of black; -1% tracking on display, +3% on small caps; 0.85 line-height on mega type; two easing curves (quad for colour, expo-out for movement); pink chip as co-brand lockup; audio version button.

## 9. UX
Strong first impression, sticky sub-nav and an audio version. Costs: a 20,190 px single page, scroll-reveals leave long blank areas until triggered (and for crawlers and screenshots), mega type clips on mobile if not scaled, white on pink fails contrast, and the line-height of 0.85 makes multi-line wraps tight.

## 10. Craft signals
- Mega headlines at 208/240/320 px with tracking and line-height in step.
- Ink is a tinted near-black, giving the pink a cooler partner.
- All reveals share one expo-out curve; colour fades share a gentle quad curve.
- The pink chip, pink pill menu and pink field form one repeating shape language.
- Voice is applied to the guideline copy itself ("Hej.").
- Cards have 78 px radius to echo phone corners.

## 11. Reproduction recipe
```css
:root{--pink:#ffa8cd;--ink:#0b051d;--cream:#f9f8f5;--lav:#efeff6;--out:cubic-bezier(.25,.46,.45,.94);--expo:cubic-bezier(.19,1,.22,1)}
body{background:#fff;color:var(--ink);font:400 20px/28px KlarnaText,sans-serif;letter-spacing:-.2px}
.mega{font:700 208px/176.8px KlarnaTitle,"Oswald",sans-serif;letter-spacing:-2.08px}
.h1{font:700 145px/145px KlarnaTitle,sans-serif}
.manifesto{background:var(--pink);font:700 80px/80px KlarnaTitle,sans-serif;letter-spacing:-.16px;padding:100px 0}
.pill{border-radius:20px;height:40px;padding:0 24px;font:500 16px/17.6px KlarnaText;background:#fff;transition:background-color .3s var(--out)}
.pill--pink{background:var(--pink)}
.chip{background:var(--pink);border-radius:8px;padding:4px 10px;font:700 24px KlarnaTitle}
.card--phone{width:291px;height:630px;border-radius:78px;overflow:hidden}
.reveal{opacity:0;transform:translateY(40px);transition:transform .8s var(--expo),opacity .56s var(--out)}
.reveal.in{opacity:1;transform:none}
.caps{font:400 12px KlarnaText;letter-spacing:.36px;text-transform:uppercase}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Pink and ink, mega type and surreal photography make an instantly recognisable look. |
| Originality | 8 | A cat under a curtain as hero, inline-image headlines and a voice-led manifesto. |
| Usability | 6 | Sticky sub-nav and audio help, but a 20,000 px page, reveal-dependent content and tight mega type. |
| Craft | 8 | Consistent tracking, line-height and easing system; custom fonts; reveal timing left blank in capture. |
