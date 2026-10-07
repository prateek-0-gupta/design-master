---
id: insp-wafer-page
source: inspora
category: Web
status: analyzed
title: "Wafer page"
creator: "@kazarov_d"
styles: [dither-halftone, glassmorphism, dark-premium, photo-led]
patterns: [ascii-rendered-painting-backdrop, centered-auth-card, oauth-pill-pair, onboarding-checklist-card, model-pricing-cards, icon-rail-sidebar, mono-capability-tags, rgb-glow-border]
mode: mixed
palette: ["#99aea9", "#889895", "#75837d", "#000000", "#2a2826", "#9a9074", "#ada183", "#c1c2ae"]
type_families: ["Helvetica Now Display / Neue Haas Grotesk-style (likely)", "Geist Mono / JetBrains Mono (tags, likely)"]
type_class: [neo-grotesk, mono]
radius_px: [32, 24, 16, 9999]
motion: {durations_s: [0.37, 0.57, 0.20, 0.73, 0.23, 0.63, 0.63], easing: [ease-out, ease-in-out], loop: true}
scores: {aesthetics: 9, originality: 8, usability: 6, craft: 8}
craft_signals: [ascii-glyph-mosaic-over-oil-painting, focus-ring-iridescent-gradient, checklist-card-rgb-edge-glow, mono-tags-vs-sans-prices, black-rail-frames-app, pricing-grid-four-columns-right-aligned-context]
anti_patterns: [white-on-sage-fails-aa, translucent-cards-low-contrast-labels]
---
# Wafer page — @kazarov_d

## 1. Snapshot
- **Subject:** A 2938×2160, 12.0 s seamless-loop flow for "Wafer", a serverless LLM API. It runs from sign-up (a dark glass card over a classical seascape painting rendered as ASCII and pixel mosaic), through typing email and password, into a dashboard of onboarding and model pricing cards over a pixelated sky, and back to the painting.
- **Why it's remarkable:** The backdrop fuses a Romantic oil painting with a terminal. The castle, sea and clouds are re-rendered with monospace glyphs ("@", "e", "$", ":") and dot grids, so "old-world craft meets API" is told by texture alone.

## 2. Composition & layout
The app is shown inside a black device frame (radius ~32 px) on a blurred sky, at about 82% of the capture width.
- **Auth state:**
  - A centred card, ~430×520 px at frame scale (about 30% of the frame width).
  - Logo tile ~54 px, title ~24 px, sub ~15 px.
  - Two OAuth pills (GitHub, Google) side by side.
  - Email and password fields (~280×40) and a white pill CTA "Create an Account".
  - A divider and a "Log In" link.
  - Terms text sits on the black frame below the painting.
- **Dashboard:**
  - A black icon rail (~230 px expanded, ~55 px collapsed).
  - A centred content column of ~1040 px (frame scale): a 2-line H1 (~46 px), a sub, a black "Get Started" checklist card, then model cards (Kimi-K3, GLM-5.2, GLM-5.1, DeepSeek-V4-Flash, Kimi-K2.6).
  - Each card has a description, mono capability tags and a 4-column price row (Input / Output / Cache / Context, with Context right-aligned).
- **Expanded card:** One card expands to a code block ("Copy & Run" with cURL, "Require ZDR" toggle, Reasoning dropdown).

## 3. Typography
- **Headings:** a neo-grotesk with tight tracking (about −0.03 em) at display sizes, close to Helvetica Now Display or Neue Haas.
  - H1 "Welcome to Wafer. Let's set up your serverless LLM." at Medium 500, ~46 px, ~1.05 leading.
  - Card descriptions ~19 px; prices ~26 px regular with lining figures.
- **Tags:** "Coding", "Agentic", "Multimodal", "Long-horizon" in a ~16 px mono, a "machine attribute" voice against the human sans.
- **Wordmark:** lowercase "wafer" in the expanded sidebar.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #99aea9 / #889895 | sage sky (dashboard field) | 50% |
| #75837d / #6e7366 | translucent card fill over sky | 13% |
| #000000 / #151517 | frame, rail, checklist card, logo tile | 16% |
| #2a2826 (est.) | auth card (smoky glass) | — |
| #9a9074 / #ada183 / #c1c2ae | sand, cloud, painting highlights | 18% |
| RGB gradient (magenta→blue→green→amber) | checklist card glow, focused-input ring | <1% |

WCAG checks:
- Auth card: white on #2a2826 is **14.69:1**, and the grey sub (~#9a9a96) is **5.2:1**.
- The CTA is black on white at 21:1.
- **Dashboard problems:**
  - The H1 (white) on the sage sky #99aea9 is **2.34:1**, which fails even large-text AA.
  - Card text on the #75837d translucent fill is **3.96:1** (large only).
  - Card labels "Input/Output" (~#d0d6d3) on #99aea9 are **1.59:1**.
  - The sub-line under the H1 is ~2.5:1.

The calm sage world costs legibility.

## 5. Depth & material
- **Auth card:** smoky dark glass (~85% #2a2826) with a soft backdrop blur, radius ~24 px and a 1 px lighter top edge.
- **Model cards:** light translucent glass (white at ~15% over the sky), radius ~24 px, no shadow.
- **Checklist card:** solid black with a **thin iridescent gradient border glow** (magenta, blue, green, amber) and a starburst of 1 px lines radiating from a white logo tile. It reads as a "power-up" object.
- **Input focus:** The focused input gets the same rainbow-gradient 1 px ring (seen at 2.01 s and 3.34 s), so the onboarding visual language starts at the very first field.
- **Backdrop:** a pixel/ASCII-dithered painting with dot-grid "sky" texture. In the dashboard, the clouds are pixel-mosaic, the same rendering at a lower density.

## 6. Components & patterns
- **Auth card:** OAuth pills, an "or" divider, inputs with a password reveal eye, a full-pill primary button and a secondary "Log In" link.
- **Sidebar:** a black icon rail (Models, API Keys, Usage, Billing, Teams; Docs, Balance "$43.42", user). It collapses to icons only after first load.
- **Onboarding checklist:** three steps with check circles, a "2/3 Completed" progress ring and a chevron on the next step.
- **Model card:** icon plus name, description, capability tag chips, a price grid and a collapse chevron. Expanding reveals the code sample with language and ZDR toggles.
- **Search:** a pill top-right with a "/" keyboard hint.

## 7. Motion
- **Measured:** 12.03 s at 30 fps, motion_fraction **0.28**, 7 segments with a median of **0.57 s**; **seamless_loop_likely = true** (first/last diff 1.63).
- **Segments:**

  | Time (s) | Duration (s) | Curve | Probable action |
  |---|---|---|---|
  | 0.13–0.50 | 0.37 | ease-in | intro |
  | 4.33–4.90 | 0.57 | symmetric | auth → dashboard transition (painting dissolves to sky) |
  | 5.97–6.17 | 0.20 | — | sidebar collapse |
  | 7.00–7.73 | 0.73 | ease-out | scroll |
  | 8.00–8.23 | 0.23 | — | card expand |
  | 9.17–9.80 | 0.63 | ease-out | scroll |
  | 10.70–11.33 | 0.63 | ease-out | return to the painting |

- **Typing (0.67–3.34 s)** is below threshold.
- **Pattern:** Ease-out dominates the scrolls (peak 0.18–0.30), and the content transitions are kept within 0.2–0.73 s.

## 8. Brand system
n/a — not a brand system. Identity cues:
- an "a"-in-rounded-square logomark (white on black or the reverse);
- a classical painting rendered as ASCII and pixels;
- black hardware-like framing;
- an iridescent gradient reserved for "progress/activation" moments.

## 9. UX
- **Strengths:**
  - A frictionless sign-up with OAuth first.
  - The onboarding checklist with a progress ring tells the user exactly what is next.
  - Pricing is transparent per model, in a consistent four-column grid.
  - Code is available in-card.
- **Weaknesses:**
  - The dashboard's white-on-sage text fails AA badly.
  - Translucent cards over a moving or pixelated background make figures harder to scan.
  - The collapsed icon rail has no labels.

## 10. Craft signals
- The ASCII glyph density varies with luminance: dense "@e$" in the castle shadows, sparse dots in the sky.
- The iridescent ring appears both on the focused input and on the checklist card border, so the activation colour carries through.
- Mono is used only for capability tags and code; prices stay in the sans.
- The Context column is right-aligned against three left-aligned price columns, separating a different unit.
- The black frame and rail double as the app's "hardware".
- The auth card's inner field radius (~10 px) sits inside a ~24 px card radius.

## 11. Reproduction recipe
```css
:root{--sky:#99aea9;--glass-light:rgba(255,255,255,.14);--glass-dark:rgba(32,30,28,.86);--ink:#fff;--frame:#000;
  --r-frame:32px;--r-card:24px;--r-field:10px;--font:"Helvetica Now Display","Neue Haas Grotesk Display",Inter,sans-serif;--mono:"Geist Mono",ui-monospace,monospace;
  --iris:linear-gradient(90deg,#ff3fd0,#4a6bff,#38e0a0,#ffc247)}
.auth{background:var(--glass-dark);backdrop-filter:blur(20px);border-radius:var(--r-card);box-shadow:inset 0 1px 0 #ffffff1a;padding:32px;color:var(--ink)}
.field{background:#ffffff0f;border-radius:var(--r-field);padding:10px 12px;border:1px solid transparent}
.field:focus-within{border:1px solid transparent;background:linear-gradient(#2a2826,#2a2826) padding-box,var(--iris) border-box}
.btn-primary{background:#fff;color:#000;border-radius:9999px;padding:10px 22px;font:500 15px var(--font)}
.checklist{background:#000;border-radius:var(--r-card);position:relative;isolation:isolate}
.checklist::before{content:"";position:absolute;inset:-1px;border-radius:inherit;background:var(--iris);filter:blur(6px);opacity:.6;z-index:-1}
.model{background:var(--glass-light);border-radius:var(--r-card);padding:20px 24px;color:#fff}
.model .tags{font:400 16px var(--mono);display:flex;gap:16px}
.model .prices{display:grid;grid-template-columns:repeat(3,auto) 1fr;gap:56px}.model .prices :last-child{text-align:right}
/* readable dashboard heading over sage: add scrim */
.dash h1{color:#fff;text-shadow:0 1px 24px rgba(40,55,50,.55)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A painting-as-ASCII backdrop with black hardware framing is evocative and cohesive. |
| Originality | 8 | The classical-art-meets-terminal texture and iridescent "activation" accents are distinctive for a dev tool. |
| Usability | 6 | An excellent onboarding flow, undermined by failing contrast on the dashboard's sage surfaces. |
| Craft | 8 | Consistent radii, mono/sans roles and the activation-colour logic; contrast is the gap. |
