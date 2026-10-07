---
id: insp-ai-prompt-bar
source: inspora
category: Product
status: analyzed
title: "AI prompt bar"
creator: "@socoloffalex"
styles: [glassmorphism, aurora-glow, micro-interaction]
patterns: [prompt-bar-with-mode-chips, typewriter-placeholder, orb-to-dot-loader-morph, frosted-panel-over-color-bloom, icon-tray-under-glass]
mode: light
palette: ["#fbe9de", "#ffffff", "#ebd7cd", "#ca6b40", "#e58951", "#ec9f6d", "#eaa896", "#1a1a1a"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [120, 96, 64, 9999]
motion: {durations_s: [8.03], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 6, craft: 7}
craft_signals: [warm-tinted-glass-not-white, orange-rim-band-behind-panel, hairline-chip-borders, orb-swaps-to-dot-spinner, placeholder-fade-in-per-word]
anti_patterns: [white-icons-on-light-gradient, cropped-composition-hides-send-action]
---
# AI prompt bar — @socoloffalex

## 1. Snapshot
- **Subject:** An 8.0 s, 3840×2160 close-up of an AI prompt bar. A frosted cream panel holds a placeholder line and three mode chips (Attach, Search, Study). It sits on a larger tray whose backdrop is a blurred orange, amber and pink bloom, with three tool icons below.
- **Why it's remarkable:** The glass is tinted warm (#fbe9de) rather than white. That lets the orange bloom bleed through and makes the whole object read as one warm material instead of a white card floating on a gradient.

## 2. Composition & layout
- The frame is a deliberate crop. The tray starts at x≈500 px (of 3840), y≈140 px, and runs off the right edge, and its bottom edge sits at y≈2020. Only the left ~55% of the bar is shown.
- **Inner prompt panel:** from x≈600 to past the edge, y≈240→1060 (about 820 px tall at 4K, about 410 px at 2×). The leading icon is at x≈810. The text starts at x≈1020, which leaves a gutter of about 100 px between icon and text.
- **Chips row:** at y≈700–950. Chips are about 250 px tall at 4K (≈62 px at 1×) with gaps of about 75 px.
- **Lower tray:** three icon slots on a ~720 px pitch: history (active, inside a 530 px rounded square), expand, and AR/scan.
- **Hierarchy:** prompt text, then chips, then tool tray. The bloom centres under the active history button and acts as a spotlight.

## 3. Typography
- One neo-grotesk, close to Inter (single-storey "g" is absent; a double-storey "a" with a flat terminal on "t"). Weight is Regular 400 throughout.
- **Prompt text:** about 120 px at 4K (≈30 px CSS) in warm grey. **Chip labels:** about 128 px at 4K, near-black #1a1a1a, so the chips carry slightly more weight than the prompt.
- Tracking is neutral to slightly open. The labels are sentence case and single words.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #fbe9de | frosted panel fill | 31% |
| #ffffff | page canvas | 17% |
| #ebd7cd / #dfbdb3 | lower tray glass, panel shading | 23% |
| #ca6b40 / #e58951 | burnt-orange bloom core, top rim band | 9% |
| #ec9f6d / #eaa896 | amber and peach mid-tones | 10% |
| #1a1a1a | chip labels, icons | <2% |

WCAG checks (contrast.py):
- Prompt text ≈#5e5450 on #fbe9de: **6.23:1** (pass).
- Chip label #1a1a1a on #f6e6dc: **14.31:1**.
- White expand and scan icons on the bloom (≈#e29a80 / #ec9f6d): **2.29:1 and 2.15:1 (fail, even for 3:1 non-text)**. The scan icon is nearly invisible.

## 5. Depth & material
- There are three planes: the white canvas, the tray (a blurred colour field with a 1–2 px lighter rim and a soft outer feather), and the frosted prompt panel. The panel has a faint drop shadow below it of about 40 px blur at 4K and a white top edge.
- A thick orange band (about 100 px at 4K) peeks above the panel. It reads as the coloured tray's top edge, seen through the panel's offset, and gives the bar a lit lip.
- The active history button is a glass square with a 2 px white inner stroke and a peach-to-amber gradient fill. Selection is shown by material, not by colour change.

## 6. Components & patterns
- **Prompt field** with a leading identity glyph that changes state: a gradient orb when idle, and a 4-dot loader when thinking.
- **Mode chips:** pill-shaped, 1 px hairline border (≈#e0c9bf), icon plus label, no fill.
- **Tool tray:** three icon buttons. Only the active one gets a container.
- Typewriter placeholder: "Ask anything" and then "Help me to create a marketing campaign" fade in word by word.

## 7. Motion
- Measured: 8.03 s at 30 fps. `motion_fraction` is 0.0 and mean energy is 0.03, so **no segment crosses the threshold**: every change is small and local. `seamless_loop_likely: true`.
- **From the frames (estimates):**
  - 0.45 s: the placeholder words "anything" are still fading in.
  - By 1.34 s: full opacity. The word reveal is about 0.3 s per word.
  - 3.12 s: the second prompt is mid-reveal.
  - 4.02 s: the orb has been replaced by a 2×2 dot grid.
  - 4.91 s: the grid collapses to a single dot.
  - 5.80–7.59 s: the dots re-form and rotate (quad, triangular scatter, quad), a "thinking" loader roughly 0.9 s per pose.
- The bloom drifts very slightly between frames, which reads as a slow linear breathing.

## 8. Brand system
n/a — not a brand system. Identity cues: a warm sunset bloom, an iridescent orb as the AI's "face", and frosted cream glass.

## 9. UX
- The mode chips make capabilities discoverable without a menu. The orb-to-dots swap gives in-place feedback without a separate spinner.
- **Risks:**
  - The send action is never shown (cropped).
  - The white tray icons fail contrast on the bloom.
  - The "thinking" state starts while the text is still a placeholder colour, so it is ambiguous whether text was submitted.

## 10. Craft signals
- The panel fill is warm-tinted #fbe9de rather than white, so glass and bloom share hue.
- The chips use a 1 px warm-grey hairline, not a grey fill, which keeps them light on glass.
- Radii are nested: tray ≈120 px, panel ≈96 px, chips fully round, active square ≈64 px (at 4K), each stepping inward.
- The loader is made from the same 4 dot positions recombined, not a stock spinner.
- The placeholder reveals per word with an opacity ramp (visible half-faded "anything" at 0.45 s).

## 11. Reproduction recipe
```css
:root{
  --glass:#fbe9dee6; --tray:#ebd7cd; --ink:#1a1a1a; --ink-2:#5e5450;
  --bloom-1:#ca6b40; --bloom-2:#e8a33a; --bloom-3:#f2a6c4; --hair:#e0c9bf;
  --r-tray:30px; --r-panel:24px; --r-btn:16px;
}
.tray{position:relative;border-radius:var(--r-tray);overflow:hidden;
  background:radial-gradient(40% 55% at 45% 65%,var(--bloom-1),var(--bloom-2) 35%,var(--bloom-3) 60%,transparent 80%),
             linear-gradient(#e58951 0 24px,#ebd7cd 24px);}
.panel{margin:12px;border-radius:var(--r-panel);background:var(--glass);
  backdrop-filter:blur(40px) saturate(1.3);box-shadow:0 10px 30px -10px #ca6b4033,inset 0 1px 0 #fff;}
.chip{border:1px solid var(--hair);border-radius:9999px;padding:8px 16px;font:400 16px/1 Inter,sans-serif;color:var(--ink)}
.tool.is-active{border-radius:var(--r-btn);background:linear-gradient(135deg,#e9a48c,#eeb877);box-shadow:inset 0 0 0 1px #ffffffaa}
.word{opacity:0;animation:in .3s ease-out forwards}
@keyframes in{to{opacity:1}}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Warm, cohesive glass where the bloom and panel share one hue family. |
| Originality | 6 | Prompt bar with chips is now standard; the warm tint and dot-loader morph are the fresh parts. |
| Usability | 6 | Clear modes and an in-place loader, but white icons on the bloom fail and there is no visible send. |
| Craft | 7 | Nested radii and hairlines are careful; the crop and invisible scan icon cost points. |
