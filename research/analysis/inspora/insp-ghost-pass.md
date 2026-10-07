---
id: insp-ghost-pass
source: inspora
category: Motion
status: analyzed
title: "ghost pass"
creator: "@lochieaxon"
styles: [soft-3d, playful-rounded, aurora-glow, micro-interaction]
patterns: [3d-ticket-hero, staggered-content-reveal, copy-code-field, primary-secondary-pill-ctas, cursor-tilt-card, light-ray-burst-intro, two-tone-headline]
mode: light
palette: ["#e1ddfe", "#f2effe", "#ffffff", "#8b78f2", "#9985d6", "#2a2730", "#5f5d66", "#9a98a0"]
type_families: ["Aeonik / Satoshi-style geometric grotesk (likely)", "SF Mono Bold (likely)"]
type_class: [geometric-sans, mono]
radius_px: [9999, 40]
motion: {durations_s: [0.9, 0.43, 0.3, 0.47, 1.23], easing: [ease-out, linear], loop: false}
scores: {aesthetics: 9, originality: 8, usability: 7, craft: 9}
craft_signals: [perforated-ticket-stub, contact-shadow-separated-from-object, mono-for-redeem-code, staggered-reveal-order, accent-word-in-headline, tinted-secondary-button, platform-aware-footnote]
anti_patterns: [white-on-lavender-button-3-5-to-1, footnote-grey-fails-aa]
---
# ghost pass — @lochieaxon

## 1. Snapshot
- **Subject:** A 13.0 s, 2336×1866 recording of an invite landing page. A glossy 3D ticket (a ghost mascot, two green coins and an "aave" stub) flies in on a burst of light rays. Then a headline, a redeem code with "Copy code" and two pill CTAs are revealed. Hovering the cursor tilts the ticket in 3D.
- **Why it's remarkable:** It turns a crypto waitlist code into a collectible, physical-feeling gift. Every UI element underneath is lavender-tinted, so the page feels like part of the object.

## 2. Composition & layout
- A single centred column. The ticket is about 640×450 px (rotated about −12°) in the top 35% of the frame. It floats about 150 px above a soft elliptical contact shadow at y≈770.
- **Headline** at y≈970 (cap height ≈95 px), about 1670 px wide. **Subhead** follows at about 48 px gap: two lines, centred, about 640 px measure.
- **Code field:** a pill about 845×140 px, with the "Copy code" button (about 275×100 px) nested inside its right end.
- **CTA row:** primary "Download on iOS" (about 535×120 px) and secondary "Join Android & Web Waitlist" (about 690×120 px), with a 40 px gap.
- **Footnote:** two lines at the bottom, about 32 px text.
- **Vertical rhythm:** headline → 60 px → sub → 90 px → code → 60 px → CTAs → 70 px → footnote.

## 3. Typography
- The headline is a geometric grotesk with tight tracking of about −0.03 em, semibold, at about 115 px real. It is close to Aeonik or Satoshi; the single-storey "a" and round "o" fit.
- **Two-tone headline:** "You've been sent a" in #2a2730, and "Ghost Pass" in lavender #8b78f2.
- **Subhead:** about 46 px regular #5f5d66 with leading of about 1.3.
- **Code:** "7UG9VBMW" in a bold monospace (SF Mono-like) at about 55 px with tracking of about +0.08 em. Using mono makes 0/O and 1/I distinguishable, which suits a code meant to be retyped.
- **Buttons:** about 40 px medium. **Footnote:** about 32 px #9a98a0.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #e1ddfe | top lavender haze, ray glow | 43% |
| #ffffff | lower page | 41% |
| #f2effe | code field and secondary button fill | 8% |
| #8b78f2 (≈#9985d6 sampled) | primary button, accent words | 4% |
| #2a2730 | headline ink | — |
| #5f5d66 / #9a98a0 | body / footnote grey | — |
| ≈#8ee86a | green coins (only complementary pop) | <1% |

WCAG checks:
- Headline #2a2730 on the haze is 13.45:1.
- Subhead #5f5d66 is 6.23:1.
- White on the #8b78f2 primary button is **3.46:1**, which passes only because the button text is large (about 40 px real, ≈20 CSS semibold).
- Secondary text (≈#6c55e0) on #f2effe is 4.62:1.
- The footnote at #9a98a0 is **2.85:1, a fail**.

## 5. Depth & material
- **Ticket:** a thick, chunky card about 14 px deep, with a darker violet bottom edge (an extruded side) and a holographic pink-to-lilac face.
- The stub is separated by a perforated (zig-zag) edge and two semicircle notches of about 20 px radius.
- The ghost is a soft subsurface-scattered blob with a rim glow.
- **Contact shadow:** a detached, blurred ellipse of about 330×30 px, lavender rather than grey, placed well below the card to sell the float.
- **UI:** the UI stays flat. The pills have no shadow; the code pill uses only a 2 px slightly darker rim.

## 6. Components & patterns
- **Code + copy:** the button is nested inside the field (pill-in-pill, inner inset of about 10 px).
- **CTA hierarchy:** filled lavender for the platform that works now (iOS), and a tinted lavender-on-lavender ghost for the waitlist.
- **Contextual footnote** for desktop visitors ("On a computer? …"). This is a thoughtful edge-case affordance.
- **3D tilt on hover:** at t≈5.07 s the ticket rotates about 60° on Y toward the cursor.

## 7. Motion
Measured: 57 fps, 13.0 s, `motion_fraction` 0.25.
- **0.0–0.9 s:** ticket entrance with light rays, an ease-out (peak at 0.20 of the segment). The rays fade by about 2 s.
- **Content reveal:** a stagger of short ease-out segments: 1.0–1.1 s (0.10), 1.27–1.70 s (0.43), 1.80–2.10 s (0.30) and 2.40–2.87 s (0.47). Frames confirm the order: the headline appears alone at 2.17 s, and the subhead, code, CTAs and footnote are all in by 3.62 s. That is a step of about 0.15–0.3 s.
- **4.67–5.90 s:** a 1.23 s continuous segment, the cursor-driven tilt of the ticket and its return.
- **After 6 s:** a gentle idle float or bob below the detection threshold (estimate from small position shifts across frames 6.5–12.3 s).

The sequence is not looped (`first_last_diff` 16.96).

## 8. Brand system
n/a — not a brand system. Identity cues:
- the Aave wordmark rotated 90° on the stub;
- the brand's lavender-to-pink gradient;
- a ghost mascot (Aave's historic ghost) reframed as cute rather than "crypto".

## 9. UX
- **Strengths:**
  - One job (redeem), with the code visible and copyable in one tap.
  - CTAs split by platform.
  - A desktop fallback.
  - Delight from the ticket is front-loaded but does not block the content (fully visible by about 3.6 s).
- **Risks:**
  - The primary button's white text is about 3.5:1.
  - The footnote fails AA.
  - The hover tilt does nothing on touch.

## 10. Craft signals
- The perforated stub edge has semicircle notches cut into both the top and bottom edges.
- The contact shadow is detached from the card by about 150 px and tinted lavender.
- Monospace is used only for the redeem code, with widened tracking.
- The accent colour of "Ghost Pass" equals the primary button fill, so the brand word and the action share a colour.
- The secondary button uses a tinted fill (#f2effe) with accent text, not an outline.
- Reveal order runs hero → headline → sub → code → CTAs → footnote, following the reading order.

## 11. Reproduction recipe
```css
:root{--haze:#e1ddfe;--tint:#f2effe;--accent:#8b78f2;--accent-ink:#6c55e0;--ink:#2a2730;--ink-2:#5f5d66;--ink-3:#8a8890;
  --font:"Satoshi","Aeonik","Inter",sans-serif;--mono:"SF Mono",ui-monospace,monospace}
body{background:radial-gradient(120% 60% at 50% 0%,var(--haze),#fff 70%);font-family:var(--font);text-align:center}
h1{font-size:clamp(32px,5vw,58px);font-weight:600;letter-spacing:-.03em;color:var(--ink)} h1 em{font-style:normal;color:var(--accent)}
.code{display:inline-flex;align-items:center;gap:40px;padding:6px 6px 6px 22px;border-radius:9999px;background:var(--tint)}
.code span{font:700 27px var(--mono);letter-spacing:.08em}
.btn{border-radius:9999px;padding:16px 28px;font-weight:500;font-size:20px}
.btn-primary{background:var(--accent);color:#fff} .btn-secondary{background:var(--tint);color:var(--accent-ink)}
.ticket{transform:perspective(900px) rotateX(var(--rx)) rotateY(var(--ry)) rotate(-12deg);transition:transform .6s cubic-bezier(.2,.8,.2,1);animation:float 4s ease-in-out infinite}
@keyframes float{50%{translate:0 -8px}}
.reveal>*{opacity:0;translate:0 12px;animation:in .45s cubic-bezier(.2,.8,.2,1) forwards}
.reveal>*:nth-child(n){animation-delay:calc(1s + var(--i) * .2s)}
@keyframes in{to{opacity:1;translate:0 0}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | A cohesive lavender world with a charming 3D hero and crisp type. |
| Originality | 8 | Reframing a waitlist code as a collectible ticket gift is fresh. |
| Usability | 7 | Clear single flow and fallback text, but the button and footnote contrast are weak. |
| Craft | 9 | Perforation, detached tinted shadow, mono code and a disciplined stagger. |
