---
id: insp-model-router
source: inspora
category: Product
status: analyzed
title: "Model router"
creator: "Maxim Kuznetsov (@disarto_max)"
styles: [data-dense, hairline-ui, technical-wireframe, micro-interaction]
patterns: [sankey-like-traffic-split, particle-flow-on-edges, cost-balanced-quality-segmented, hover-to-isolate-route, inline-share-bars-in-table, sentence-style-fallback-rule, dirty-state-deploy-button]
mode: light
palette: ["#f3f2f7", "#ffffff", "#e6e5ea", "#d8d0d3", "#111111", "#e2532d", "#5b5bd6", "#c2185b"]
type_families: ["Inter (likely)", "JetBrains Mono / Berkeley Mono-style mono (likely)"]
type_class: [neo-grotesk, mono]
radius_px: [28, 22, 9999]
motion: {durations_s: [20.03], easing: [linear], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 8, craft: 9}
craft_signals: [particles-encode-throughput-per-edge, route-colour-consistent-across-chart-table-dropdown, mono-uppercase-eyebrows, deploy-button-dims-when-no-changes, hover-dims-siblings-to-30pct, diagonal-hatch-canvas-with-dashed-guides]
anti_patterns: [light-grey-mono-rates-fail, dimmed-deploy-white-text-2-1]
---
# Model router — Maxim Kuznetsov

## 1. Snapshot
- **Subject:** A 20 s, 3024×1896 recording of a "Model router" panel. A gateway node splits traffic into four curved edges (Opus 5.5, GPT-6.1 Sol, Haiku 4.5, Qwen3.5 9B) with particles flowing along them.
  - A Cost / Balanced / Quality segmented control re-weights the split live; the blended cost reacts, e.g. $0.0026 "44% vs live" on Cost and $0.0089 "93% vs live" on Quality.
  - Below: a routes table (share, P50/P95, $/1K, errors), a sentence-style fallback rule, and a Deploy policy footer.
- **Why it's remarkable:** It makes an abstract routing policy tangible. Particle density and edge thickness show the traffic share, and the same colours tie the chart, table and dropdowns together.

## 2. Composition & layout
- **Panel:** about 740×875 px in the 2000-px key frame (≈1120×1320 native), centred on a #f3f2f7 canvas with diagonal hatching and dashed vertical guides at the panel edges (x≈628 and 1372).
- **Structure:** a grey shell (radius ≈28 px) containing two white inner cards (radius ≈22 px) and a footer.
  1. Header: "Model router", info icon, a "chat-prod" environment select, a settings icon and ✕.
  2. Hero card: eyebrow "BLENDED COST · LIVE POLICY"; "$0.0046" at about 50 px with "/ 1K tokens"; a mono stats line "330 REQ/S · P95 1.26 S · 0.50% ERRORS"; and the flow chart (gateway at x≈668, endpoints at x≈1163 with labels and a mono rate "56/S").
  3. Routes card: a 4-row table on a 53 px row pitch, then the fallback rule row.
  4. Footer: a kebab menu, mono "POLICY V14 · LIVE ON CHAT-PROD", and the "Deploy policy" pill on the right.

## 3. Typography
- **Sans** (Inter-like) for names and values:
  - title 22 px Medium;
  - hero number about 50 px Medium with tabular numerals;
  - table about 18 px.
- **Mono uppercase** at about 14 px with +0.08 em tracking for eyebrows, column headers ("P50 / P95 S", "$ / 1K"), provider tags ("ANTHROPIC", "SELF-HOSTED"), rates and the policy status.
- Numbers in the table are sans with tabular figures. The convention is mono for metadata and labels, and sans for primary values.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #f3f2f7 | canvas, panel shell | 81% |
| #ffffff | inner cards | 13% |
| #e6e5ea / #d8d0d3 | hairlines, segmented-track borders, hatch | 6% |
| #111111 | primary values | <1% |
| ≈#5b5bd6 / ≈#4fb89a / ≈#b06ce0 / ≈#c2185b | route colours: Opus indigo, GPT teal, Haiku violet, Qwen magenta | <1% |
| ≈#e2532d | fallback toggle, Deploy button (dirty state) | <1% |

WCAG checks (contrast.py):
- Values #111 on white: **18.88:1**.
- Grey sans text ≈#8a8a8f: **3.44:1**. Dimmed mono rates and provider tags ≈#b8b8bd: **1.98:1 (fail)**.
- The Qwen magenta label ≈#c2185b: **5.87:1**.
- Deploy button white on the active orange #e2532d: **3.81:1 (large only)**. On the disabled tint ≈#f0a08a: **2.08:1**, which is intentional as a disabled state but still unreadable.
- Footer mono ≈#6e6e73 on #f3f2f7: **4.55:1**.

## 5. Depth & material
- **Shell:** a soft wide shadow (about 0 30px 60px rgba(20,20,40,.08)). The inner cards have a 1 px #e6e5ea border and no shadow.
- **Segmented control:** the selected thumb is white with a small shadow on a hairline track.
- **Chart edges:** about 2 px lines at about 40% opacity, with solid particles (3–5 px dots) travelling along them and a glow halo on the endpoint nodes.

## 6. Components & patterns
- **Flow chart:** a gateway node fanning into bezier edges to model nodes, with live rates at the endpoints.
- **Segmented strategy picker:** COST / BALANCED / QUALITY, in mono caps.
- **Delta tag:** "▾ 44% VS LIVE" in green and "▴ 93% VS LIVE" in orange next to the eyebrow when a draft differs from the live policy.
- **Routes table:** a colour dot, model name, provider tag, a mini share bar plus %, latency pair, cost and error rate.
- **Fallback rule** written as a sentence: [toggle] Fallback if [Opus 5.5 ▾] fails, retry on [GPT-6.1 Sol ▾]. The dropdown is headed "IF THIS MODEL FAILS" and lists models with their costs.
- **Dirty-state footer:** "UNSAVED CHANGES" replaces "LIVE ON CHAT-PROD", and Deploy turns from pale to solid orange.

## 7. Motion
- Measured: 20.03 s at 57 fps. `motion_fraction` is **0.0** with no segments; mean energy is 0.07 and p95 0.16. The motion is continuous low-amplitude particle flow (linear), and it loops (`seamless_loop_likely: true`).
- **From frames (estimates):**
  - 3.34 s: Cost is selected, and the edge thickness re-weights (Haiku 49%, Qwen 24%, Opus 6%).
  - 5.56 s: Quality is selected (Opus 58%), and the Opus edge thickens with a halo.
  - 7.79 s and 10.02 s: hovering a route dims the other edges and table rows to about 30%.
  - 12.24 s: the fallback toggle is turned off and the rule row greys out.
  - 14.47–16.69 s: the fallback dropdown is open and the models are swapped.
- The state changes appear to be quick crossfades and width tweens (<0.3 s). They fall under the measurement threshold because the panel is small in frame.

## 8. Brand system
n/a — not a brand system.

## 9. UX
- Excellent for a technical user. The "what if" is shown before deploy (a delta versus live). Hover isolates a route across the chart and table at once. The fallback is readable as plain language. The deploy button signals the dirty state.
- **Risks:**
  - The dimmed mono rates are below 2:1.
  - Route colours (indigo, violet) are close to each other for colour-vision deficiency; the labels mitigate this.
  - The orange Deploy fails AA for normal text.

## 10. Craft signals
- Each route's colour is identical in the chart edge, table dot, share bar and dropdown dot.
- Particles flow faster and denser on higher-share edges, which encodes throughput, not just decoration.
- The eyebrow line switches between "LIVE POLICY" and "SAME AS LIVE", with a delta tag when changed, so state is spelled out.
- Hovering a model dims siblings consistently in both the chart and the table.
- The canvas uses diagonal hatching with dashed guides aligned to the panel edges, a blueprint framing.
- Mono is used only for metadata and labels; primary numbers are tabular sans.

## 11. Reproduction recipe
```css
:root{--canvas:#f3f2f7;--card:#fff;--line:#e6e5ea;--ink:#111;--ink-2:#6e6e73;--ink-3:#8a8a8f;
  --opus:#5b5bd6;--gpt:#3fae8c;--haiku:#b06ce0;--qwen:#c2185b;--action:#c94420;--r-shell:28px;--r-card:22px;
  --mono:"JetBrains Mono",ui-monospace,monospace}
body{background:var(--canvas) repeating-linear-gradient(135deg,#0000 0 10px,#00000008 10px 11px)}
.shell{background:var(--canvas);border-radius:var(--r-shell);padding:6px;box-shadow:0 30px 60px -20px #14142814}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r-card);padding:20px 24px}
.eyebrow,.th,.tag{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
.hero{font:500 40px/1 Inter;font-variant-numeric:tabular-nums}
.edge{fill:none;stroke-width:2;opacity:.4;transition:opacity .2s,stroke-width .3s}
.flow:has(.route:hover) .route:not(:hover){opacity:.3}
.particle{offset-path:var(--d);animation:travel var(--t,2.4s) linear infinite}
@keyframes travel{from{offset-distance:0%}to{offset-distance:100%}}
.deploy{background:var(--action);color:#fff;border-radius:9999px;padding:8px 16px}   /* #c94420 → 4.9:1 */
.deploy:disabled{opacity:.45}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Calm, technical and well-proportioned; the particle flow adds life. |
| Originality | 8 | Particle-flow routing plus a sentence-style fallback is a fresh pattern for infra UIs. |
| Usability | 8 | Previews, hover isolation and dirty-state clarity; some meta text is far too light. |
| Craft | 9 | Colour mapping, typographic roles and state copy are rigorously consistent. |
