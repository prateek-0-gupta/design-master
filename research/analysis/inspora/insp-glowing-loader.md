---
id: insp-glowing-loader
source: inspora
category: Motion
status: analyzed
title: "glowing loader"
creator: "@sir_hsn"
styles: [generative-particle, soft-3d, minimal-swiss, micro-interaction]
patterns: [ai-state-orb, dotted-sphere-loader, segmented-state-switcher, shimmer-status-text, state-specific-orb-forms, sliding-active-pill]
mode: light
palette: ["#fefefe", "#f3f3f2", "#f7e6d7", "#e1e9ea", "#c9bebc", "#d03a2a", "#5a5f63", "#111111"]
type_families: ["Inter (likely)"]
type_class: [neo-grotesk]
radius_px: [9999]
motion: {durations_s: [0.2, 0.13, 0.13, 0.2], easing: [ease-out, ease-in-out], loop: false}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 8}
craft_signals: [dot-size-falloff-toward-limb, warm-cool-iridescent-shell, shimmer-sweep-on-status-label, red-ring-for-your-turn, glossy-bead-for-ready, status-text-separate-from-control]
anti_patterns: [shimmer-trough-letters-low-contrast, error-state-not-shown]
---
# glowing loader — @sir_hsn

## 1. Snapshot
- **Subject:** A 20.9 s, 1072×720 demo of an AI status orb with a segmented control below it. The control holds Standby / Thinking / Building / Generating / Waiting / Error, and each state changes the orb and the caption ("Thinking…", "Writing…", "Your turn", "Ready").
- **Why it's remarkable:** One 260 px sphere carries six distinct states through form, not colour coding alone:
  - a rotating dotted globe while working;
  - a red outer ring for "your turn";
  - a single glossy red bead at rest.

## 2. Composition & layout
- Single centred column on near-white #fefefe.
- **Orb:** about 260 px diameter, centred at x=536, y≈282.
- **Caption:** at y≈464, about 50 px below the orb.
- **Segmented control:** about 753×60 px at y≈514–574, roughly 70 px below the caption.
- **Rhythm:** orb : caption-gap : control is about 260 : 50 : 70. The cluster sits slightly above centre.
- **Control padding:** about 20 px on the left; the six segments have natural widths of about 90–130 px.

## 3. Typography
- Neo-grotesk (Inter-like).
- **Control labels:** about 20 px medium #5a5f63. The active label is #111 semibold on a white pill.
- **Caption:** about 20 px regular in a grey shimmer. A brighter band sweeps across ("Thin" dark, "king…" light in the key frame), the familiar "AI is thinking" text-shimmer idiom.
- Captions use a true ellipsis character, and "Your turn" / "Ready" have no ellipsis when no work is in progress.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #fefefe | canvas | 91% |
| #f3f3f2 | control track | 4% |
| #f7e6d7 / #e1e9ea | orb shell: peach (lower-left) / ice-blue (upper-right) | 3% |
| #c9bebc / #a69b9c | dim dots, faint shell rim | 1.5% |
| ≈#d03a2a | active dots, red ring, Ready bead | <1% |
| #5a5f63 / #111111 | inactive / active labels | — |

WCAG checks:
- Inactive labels #5a5f63 on #f3f3f2 are 5.82:1.
- The active label #111 on white is 18.88:1.
- The caption at its darkest (#6b6b6b) is 5.28:1. In the shimmer trough (≈#a69b9c) it drops to **2.67:1**.

## 5. Depth & material
- The orb shell is a pale iridescent sphere: a peach to white to ice-blue gradient with a slightly darker 1 px rim (≈#e8d6d2).
- Inside it, dots are arranged on a sphere. They shrink and fade toward the limb, which gives volume without any shading.
- **"Ready":** a glossy red bead about 62 px across, with a white specular dot at 10 o'clock, sitting in the middle of the empty shell.
- **Waiting / "Your turn":** a 2 px rose ring (≈#d78a86) surrounds the shell, offset about 3 px.
- **Control:** a flat track with a 1 px #e6e6e6 border. The active pill is white with a soft 1 px shadow.

## 6. Components & patterns
- **Segmented control as state demo:** the active pill slides between segments. The control exists to showcase the states; in a product the states would be driven by the system.
- **State to orb form:**
  - Thinking: sparse dots with red clusters;
  - Building / Generating ("Writing…"): denser bands that rotate;
  - Waiting: a ring;
  - Standby: a bead.
- The caption is a separate live region from the control. Its text differs from the control label ("Generating" shows "Writing…").

## 7. Motion
Measured: 60 fps, 20.9 s, `motion_fraction` 0.04. The detector only catches the larger state transitions:
- 4.63–4.83 s (0.20 s, symmetric);
- 4.93–5.07 s (0.13 s, ease-out, peak at 0.12);
- 16.50–16.63 s (0.13 s, ease-out);
- 17.20–17.40 s (0.20 s, ease-in).

Those are the pill slide and the orb swap: fast, 130–200 ms. The globe's rotation and the caption shimmer run continuously below the 0.35 threshold. From the frames, the globe turns a few degrees per second, so the dot pattern differs at 1.16, 3.48 and 5.80 s (estimate). The shimmer sweep takes about 1.5 s per pass (estimate from the dark/light letter split).

## 8. Brand system
n/a — not a brand system. The warm-peach/ice-blue shell plus a red accent could serve as an AI persona mark.

## 9. UX
- **Strengths:**
  - Distinct silhouettes per state, so meaning does not rely on colour only.
  - Captions add text redundancy.
  - Distinguishing "Your turn" from "Ready" is genuinely useful for agent UIs.
- **Risks:**
  - The Error state is never demonstrated.
  - Shimmer troughs drop below AA.
  - Continuous rotation needs a reduced-motion variant.

## 10. Craft signals
- Dot diameter and opacity fall off toward the limb, giving a spherical read without shading.
- The shell has a warm lower-left and cool upper-right, a soft iridescence.
- The waiting ring is a separate 2 px stroke offset from the shell, not a border colour change.
- The Ready bead has a specular dot at 10 o'clock, matching the shell's implied light.
- The caption verb differs from the control label ("Generating" vs "Writing…"), so it is written for the user and does not echo the system label.
- Pill transitions are 130–200 ms, kept snappy for a control.

## 11. Reproduction recipe
```css
:root{--bg:#fefefe;--track:#f3f3f2;--ink:#111;--ink-2:#5a5f63;--accent:#d03a2a;--peach:#f7e6d7;--ice:#e1e9ea}
.orb{width:260px;aspect-ratio:1;border-radius:50%;position:relative;
  background:radial-gradient(circle at 30% 75%,var(--peach),transparent 60%),radial-gradient(circle at 75% 25%,var(--ice),transparent 55%),#fff;
  box-shadow:inset 0 0 0 1px #ead9d5}
.orb[data-state=waiting]::after{content:"";position:absolute;inset:-5px;border-radius:50%;border:2px solid #d78a86}
.orb[data-state=standby]::before{content:"";position:absolute;inset:38%;border-radius:50%;
  background:radial-gradient(circle at 30% 30%,#fff 0 8%,transparent 9%),radial-gradient(circle at 40% 35%,#ff6a4a,var(--accent) 60%,#a82518)}
.caption{font:400 20px Inter,sans-serif;background:linear-gradient(90deg,#6b6b6b 40%,#c9c9c9 50%,#6b6b6b 60%) 0 0/300% 100%;
  -webkit-background-clip:text;color:transparent;animation:shimmer 1.5s linear infinite}
@keyframes shimmer{to{background-position:-150% 0}}
.seg{display:flex;padding:4px;border-radius:9999px;background:var(--track);border:1px solid #e6e6e6}
.seg button{padding:12px 18px;border-radius:9999px;font:500 20px Inter,sans-serif;color:var(--ink-2);transition:all .18s cubic-bezier(.2,.8,.2,1)}
.seg [aria-pressed=true]{background:#fff;color:var(--ink);font-weight:600;box-shadow:0 1px 2px rgb(0 0 0/.08)}
/* dotted globe: canvas, Fibonacci-sphere points, size = r*(0.3+0.7*z), rotate 15deg/s */
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | A delicate dotted globe with a warm/cool shell and a precise minimal control. |
| Originality | 8 | Per-state *forms* (globe, ring, bead) go beyond the usual colour-swap orb. |
| Usability | 8 | Clear state mapping with text redundancy. Error is missing and the shimmer dips in contrast. |
| Craft | 8 | Dot falloff, a consistent light source and snappy 130–200 ms control motion. |
