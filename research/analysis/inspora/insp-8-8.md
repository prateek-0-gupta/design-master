---
id: insp-8-8
source: inspora
category: Illustration
status: analyzed
title: "ipod AI agent"
creator: "@nilseller"
styles: [skeuomorphic, y2k-chrome, physical-material, playful-rounded]
patterns: [cover-flow-agent-picker, click-wheel-navigation, aqua-chat-bubbles, agent-avatar-as-finder-face, reflection-under-carousel, title-bar-with-battery]
mode: light
palette: ["#f5f5f7", "#bfc0c4", "#e5e6ea", "#0b0b0d", "#e6842d", "#acd0f0", "#53ae47", "#a4a3a8"]
type_families: ["Lucida Grande / Myriad (likely, iPod Classic UI)", "Helvetica Bold (labels)"]
type_class: [humanist-sans, neo-grotesk]
radius_px: [9999, 120, 28, 12]
motion: {durations_s: [0.47, 0.1, 0.13, 0.17], easing: [ease-out], loop: true}
scores: {aesthetics: 8, originality: 8, usability: 6, craft: 8}
craft_signals: [finder-face-recoloured-per-agent, glossy-reflection-fade, aqua-gel-blue-sent-bubble, period-correct-title-bar-gradient, cursor-dot-on-click-wheel, cover-flow-tilted-sides]
anti_patterns: [menu-label-low-contrast, nostalgia-over-function, trademark-pastiche]
---
# ipod AI agent — @nilseller

## 1. Snapshot
- **Subject:** An 8.7 s, 1920×1280 looping demo of an iPod Classic whose firmware has become an AI-agent client:
  - an "Agents" Cover Flow of Finder-face avatars in different colours (Lisa, Clarus, Mac);
  - pressing centre opens a "Messages" thread with that agent ("Shipped the deploy while you slept.");
  - MENU returns to the carousel.
- **Why it's remarkable:** It maps 2007 iPod navigation exactly onto agent selection and chat. The scroll wheel picks the agent and the centre button opens the conversation. Nostalgic interface conventions carry an AI product.

## 2. Composition & layout
- The iPod is cropped at the bottom, centred, ~800 px wide (x≈557–1354), with a ~120 px corner radius on a #f5f5f7 background.
- **Screen:** ~675×510 px inside a ~20 px black bezel (#0b0b0d).
  - A ~40 px title bar ("Agents"/"Messages" plus battery).
  - Content below: either the Cover Flow, where the centred cover is ~230 px with side covers tilted at about 60° and stacked, or a chat with an avatar header, bubbles and an input field.
- **Click wheel:** ~530 px diameter, with a ~195 px centre button and MENU / ⏮ / ⏭ labels. A white ~70 px circular "finger" dot shows the touch point.

## 3. Typography
- iPod-era UI fonts:
  - the title bar "Agents" is ~22 px Bold (Myriad / Lucida-like);
  - the cover label "Clarus" is ~24 px Helvetica Bold;
  - bubbles are ~20 px Regular (Lucida Grande-like, slightly wide);
  - the input placeholder "Message Clarus" is ~22 px grey.
- Wheel labels ("MENU") are ~24 px Bold with wide tracking (~0.12 em) in #a4a3a8.

## 4. Colour
| Hex | Role | Share |
|---|---|---|
| #f5f5f7 | backdrop | 71% |
| #bfc0c4 / #e5e6ea | iPod silver face / click-wheel | 21% |
| #0b0b0d | screen bezel | — |
| #e6842d (+ cyan, violet, blue, pink, green) | per-agent Finder-face colours | — |
| #acd0f0 | sent bubble (Aqua gel blue) | — |
| #f0f0f0 | received bubble | — |
| #53ae47 | battery | — |

WCAG:
- Bubble text #1a1a1a on #acd0f0 is 10.51:1, and on #ececec it is 14.73:1.
- Cover label on white is 18.88:1.
- Placeholder #8c8c8c on white is 3.36:1.
- The MENU label #a4a3a8 on the wheel #ececee is **2.12:1**, faithful to the original but failing.

Each agent is identified purely by hue: an orange, cyan, violet, blue, pink or green Finder face.

## 5. Depth & material
- **Device:** brushed or anodised silver with a vertical gradient and a soft edge shadow.
- **Click wheel:** a satin, slightly concave surface; the centre button has a subtle radial highlight.
- **Covers:** glossy 2007-style icons with a horizontal-split face, a specular sheen and a mirror reflection below at about 30% opacity that fades out over ~100 px.
- **Bubbles:** Aqua gel style, a top-light gradient plus a 1 px darker outline.
- **Title bar:** the light grey gradient of the iPod OS.

## 6. Components & patterns
- **Cover Flow picker:** the centred item is flat and large, side items are rotated and overlapped.
- **Chat thread:** an agent avatar and name header, a left grey received bubble, a right blue sent bubble, and a pill input with a round → send button.
- **Click-wheel control:** a visible touch dot shows the scroll and press positions.
- **Navigation stack:** Agents → Messages → MENU (back). At t≈8.2 s the chat bubbles fade over the carousel during the back transition.

## 7. Motion
Measured: 30 fps, duration 8.70 s, motion_fraction 0.15, 7 segments, median 0.13 s, seamless_loop_likely true.

| Segment (s) | Duration | Shape | Event |
|---|---|---|---|
| 0.43–0.90 | 0.47 s | ease-out, peak 0.11 | Cover Flow scroll from Lisa to Clarus |
| 1.90–2.00 | 0.10 s | ease-out | screen cut to Messages |
| 3.73 / 4.53 | 0.10 s | — | back to Agents |
| 4.77–4.90 / 5.20–5.37 | 0.13–0.17 s | ease-out | quick carousel steps toward Mac |
| 8.17–8.33 | 0.17 s | ease-out | Messages → Agents cross-fade |

All motion is fast-start ease-out with short durations (0.1–0.47 s), which matches the snappy original iPod OS. Long holds (~1–3 s) between actions let each screen be read.

## 8. Brand system
n/a — not a brand system. It is a deliberate Apple pastiche:
- iPod Classic hardware;
- the Finder face as an agent avatar;
- Aqua bubbles and iPod OS chrome.

The identity idea worth keeping is "one face, many hues" for a family of agents.

## 9. UX
- **Strengths:** Selecting an agent and chatting fits the iPod's two-level hierarchy well, and colour-coded avatars make agents instantly distinguishable.
- **Weaknesses:**
  - Text input on a click wheel is impractical. The demo shows an input field with no way to type.
  - The labels (2.1:1) fail contrast.
  - It is a concept piece and gives no real interaction model for writing.

## 10. Craft signals
- The Finder face is recoloured per agent while keeping the identical split-face geometry.
- Cover reflections fade out and are clipped at the screen edge.
- The sent bubble uses an Aqua-like gel gradient (#dcedff → #acd0f0) with a 1 px outline.
- The title bar has a period-correct grey gradient and a green battery glyph (#53ae47).
- A white touch dot on the wheel reveals the scroll and press location.
- Side covers are tilted and overlapped in true Cover Flow perspective.

## 11. Reproduction recipe
```css
:root{--bg:#f5f5f7;--body:#bfc0c4;--wheel:#e5e6ea;--bezel:#0b0b0d;--sent:#acd0f0;--recv:#f0f0f0;--label:#7d7c82;/* darkened for 3:1 */}
.ipod{width:800px;border-radius:120px 120px 0 0;background:linear-gradient(#d6d7da,var(--body))}
.screen{border:20px solid var(--bezel);border-radius:28px;background:#fff;overflow:hidden}
.titlebar{height:40px;background:linear-gradient(#f4f4f6,#d4d5d8);font:700 22px "Myriad Pro","Lucida Grande",sans-serif;border-bottom:1px solid #9a9a9e}
.coverflow{perspective:900px;display:flex;justify-content:center}
.cover{width:230px;aspect-ratio:1;border-radius:40px;-webkit-box-reflect:below 8px linear-gradient(transparent 60%,rgb(255 255 255/.35));transition:transform .47s cubic-bezier(.1,.8,.2,1)}
.cover.left{transform:translateX(-30px) rotateY(60deg) scale(.85)}.cover.right{transform:translateX(30px) rotateY(-60deg) scale(.85)}
.bubble{border-radius:9999px;padding:8px 18px;font:400 20px "Lucida Grande",sans-serif;border:1px solid rgb(0 0 0/.18)}
.bubble.sent{background:linear-gradient(#dcedff,var(--sent))}.bubble.recv{background:linear-gradient(#fafafa,#e6e6e6)}
.wheel{width:530px;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--wheel) 0 36%,#f2f2f4 37%,var(--wheel) 100%)}
.wheel .menu{font:700 24px Helvetica;letter-spacing:.12em;color:var(--label)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Faithful and polished 2007 Apple rendering, with a cheerful multi-hue agent set. |
| Originality | 8 | The agents-as-Cover-Flow and wheel-to-chat mapping is a witty, coherent concept. |
| Usability | 6 | Navigation maps well, but text input is impossible on the wheel and the labels fail contrast. |
| Craft | 8 | Period-accurate chrome, reflections, Aqua bubbles and snappy ease-out timing. |
