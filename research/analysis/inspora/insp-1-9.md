---
id: insp-1-9
source: inspora
category: Web
status: analyzed
title: "Footer.mp4"
creator: "@alimdesigner_"
styles: [cinematic-3d, photo-led, editorial-serif, x-day-to-night]
patterns: [illustrated-scene-footer, four-column-footer-links, day-to-night-transition, tv-test-pattern-screen, chromatic-hover-link, particle-dandelion-drift]
mode: dark
palette: ["#3668af", "#1b3272", "#283e7c", "#43547d", "#696c74", "#473622", "#8b613d", "#ffffff"]
type_families: ["condensed transitional serif for headers (likely Instrument Serif / Editorial New Condensed)", "Inter (likely)"]
type_class: [editorial-serif, neo-grotesk]
radius_px: [12]
motion: {durations_s: [0.17, 1.83, 0.37], easing: [ease-out, ease-in-out, ease-in], loop: false}
scores: {aesthetics: 9, originality: 9, usability: 7, craft: 8}
craft_signals: [footer-copy-matches-scene-story, rgb-split-underline-on-hover, test-pattern-then-screen-off, sky-darkens-behind-static-text, header-serif-vs-link-sans, glow-bleed-from-crt]
anti_patterns: [white-links-on-light-day-sky-borderline, heavy-video-for-a-footer]
---
# Footer.mp4 — @alimdesigner_

## 1. Snapshot
- **Subject:** A 7.0 s, 1902×1080 recording of a website footer for "offline". A beige 1984-style all-in-one computer sits on a grassy hill under a sky that shifts from afternoon blue to night. Its screen goes from white flash to colour-bar test pattern to black, while dandelion seeds become stars.
- **Why it's remarkable:** The footer is the story's ending. The tagline says this is everything to know "before you finally log off", and the scene literally logs off: the computer powers down as night falls.

## 2. Composition & layout
- **Top band (y≈80–290):** a four-column footer.
  - **Brand block (x≈105):** "offline" wordmark at about 46 px, a 2-line tagline at about 19 px and a copyright line at about 17 px.
  - **Link columns at x≈633, 1037 and 1441:** Platform / About / Social Media.
- Column headers sit at y≈96 and links at a 42 px rhythm (155, 197, 238, 280).
- **Bottom 70%:** the scene. The computer (about 350×420 px) sits centred at x≈950 on the crest of a hill that fills the bottom about 20%. The space between links and computer (about 200 px of sky) lets the type breathe.

## 3. Typography
- **Wordmark and column headers:** a condensed, high-contrast serif with tall x-height (Instrument Serif / Editorial New Condensed feel). The wordmark is about 46 px and headers about 32 px, regular weight, tracking about −0.01 em.
- **Links and body:** a neo-grotesk (Inter-like) at about 19 px regular, white. The copyright is about 17 px at 90% white.
- **Hover state:** on "Instagram", "How it works", "Pricing" and "Careers" (various frames) the link shows a 1 px underline plus an RGB-split chromatic glitch on the glyphs (magenta/cyan offsets of about 1 px), echoing the CRT.

## 4. Colour
| Hex | Role | Share (key frame) |
|---|---|---|
| #3668af → #547dbb | day sky (t=0.39 s, sampled) | — |
| #1b3272 / #283e7c | dusk/night sky (key) | 45% |
| #43547d / #525f7a / #696c74 | horizon haze | 31% |
| #473622 / #705331 / #8b613d | grass in sunset light | 15% |
| #827367 / #8e7d72 | computer beige shell | 7% |
| SMPTE bars | screen accent (white, yellow, cyan, green, magenta, red, blue) | <3% |
| #ffffff | all text | — |

WCAG checks:
- White on the night sky #1b3272 is 12.0:1, and on #283e7c 10.1:1.
- On the day sky the top band (#3668af) is 5.59:1, but lower-right sky (#4a7bc4 → #6b93cf) drops to 4.27:1 and 3.13:1. Links in the early frames are only borderline legible, and they get more legible as night falls.

## 5. Depth & material
- **Scene:** a soft cinematic 3D render with depth of field. The grass in the foreground is sharp, and dandelion seeds and stars float at varied sizes (4–14 px).
- **Computer:** emits a purple-blue glow halo of about 20 px when the test pattern is on. It has scan-line texture and a curved-glass vignette on the screen.
- **Text:** flat white on the scene, with no scrim, plate or shadow.

## 6. Components & patterns
- A four-column footer: brand, 4 + 4 + 3 links.
- A hover state with underline and chromatic aberration.
- An ambient scene as background: video or WebGL.
- No newsletter, socials as text links, no icons.

## 7. Motion
Measured: 7.0 s at 30 fps. motion_fraction is 0.34, there are 4 segments and the clip is not a loop (first/last diff 53.6, day ≠ night).
- **0.23–0.40 s (0.17 s, peak 0.30, ease-out) and 0.50–0.60 s (0.10 s, ease-out):** the screen's white flash and the cut to colour bars, a CRT power-on.
- **2.17–4.00 s (1.83 s, peak 0.48, ease-in-out):** the main sky transition from blue to deep navy as stars appear.
- **4.27–4.63 s (0.37 s, peak 0.86, ease-in):** the screen collapses to black (a CRT power-off accelerates into the cut). By t=5.06 s the screen is dark.
- **Links:** they fade in from about 30% opacity at t=0.39 s to full at t=1.17 s (estimated stagger by column).
- **Continuous elements:** dandelion seeds drift slowly upward and to the right, and grass sways.

## 8. Brand system
n/a — not a brand system. Identity cues:
- a lowercase serif "offline" wordmark;
- digital-detox storytelling (computer turns off, nature remains);
- retro Macintosh nostalgia;
- serif/sans pairing.

## 9. UX
- The links are standard and well grouped, and the hover feedback is clear (underline plus glitch).
- **Risks:**
  - Legibility depends on the sky state: borderline on the lighter day sky at the lower right.
  - A heavy video in the footer needs lazy loading and a reduced-motion poster.
  - The chromatic glitch on hover may harm readability for some users.

## 10. Craft signals
- The narrative sync: the tagline "before you finally log off" pairs with the computer powering off and night falling.
- The hover glitch borrows the CRT's RGB vocabulary, so interaction and scene share a language.
- All three link columns start at the same baseline (y≈155) with an even 42 px rhythm, and the headers align at y≈96.
- Column x-positions are spaced about 404 px apart (633 / 1037 / 1441), an even 3-column rhythm right of the brand block.
- The test-pattern glow spills a purple halo onto the beige shell, a physically plausible light bleed.
- Seeds and stars use the same asterisk-like glyph, so dandelions turn into stars over time.

## 11. Reproduction recipe
```css
:root{--day:#3668af;--dusk:#283e7c;--night:#1b3272;--text:#fff;
  --serif:"Instrument Serif","Editorial New",serif;--sans:Inter,system-ui}
.footer{position:relative;min-height:100vh;color:var(--text);background:var(--night)}
.footer video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1}
.footer .cols{display:grid;grid-template-columns:528px repeat(3,404px);padding:80px 105px}
.footer h4{font:400 32px/1 var(--serif);margin-bottom:28px}
.footer a{display:block;font:400 19px/42px var(--sans);color:var(--text);text-decoration:none}
.footer a:hover{text-decoration:underline 1px;text-underline-offset:4px;
  text-shadow:-1px 0 rgba(255,0,180,.8),1px 0 rgba(0,220,255,.8)}
@keyframes nightfall{from{filter:brightness(1.15) hue-rotate(-8deg)}to{filter:brightness(.55)}}
.footer video{animation:nightfall 1.83s cubic-bezier(.45,0,.55,1) 2.17s both}
@media (prefers-reduced-motion:reduce){.footer video{display:none}.footer{background:url(night-poster.jpg) center/cover}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A beautiful cinematic scene, with elegant serif headers over a calm grid. |
| Originality | 9 | A footer that acts out "logging off" through day-to-night and a CRT power-down is a genuinely new idea. |
| Usability | 7 | The links are clear and grouped. Day-state contrast is borderline and the footer is heavy. |
| Craft | 8 | Story, hover vocabulary and grid rhythm are all aligned. Text has no scrim. |
