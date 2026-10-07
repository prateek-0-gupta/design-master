---
id: insp-feature-menu
source: inspora
category: Web
status: analyzed
title: "feature menu"
creator: "@mona_biasia"
styles: [glassmorphism, dark-premium, photo-led, cinematic-3d]
patterns: [mega-menu-with-preview-pane, hover-to-preview, arrow-prefix-active-item, glass-dropdown-over-video, integration-icon-grid, skeleton-diagram-preview, pill-sign-in]
mode: dark
palette: ["#3b1a11", "#51301a", "#6f4a1c", "#e28129", "#96381d", "#aa3b1a", "#0a0f12", "#ffffff"]
type_families: ["Inter (likely)", "editorial serif for page hero, Instrument Serif-like (likely)"]
type_class: [neo-grotesk, editorial-serif]
radius_px: [32, 24, 16, 9999]
motion: {durations_s: [0.67, 0.57, 0.73, 0.7, 0.2, 0.17], easing: [ease-in-out, ease-out], loop: false}
scores: {aesthetics: 9, originality: 7, usability: 8, craft: 8}
craft_signals: [two-tier-glass-nested-panel, arrow-slides-in-on-active-row, preview-fades-title-before-content, menu-tint-inherits-hero-video-colour, empty-icon-cells-for-rhythm, skeleton-lines-as-illustration]
anti_patterns: [inactive-nav-links-low-contrast-on-orange, preview-content-delay]
---
# feature menu — @mona_biasia

## 1. Snapshot
- **Subject:** A 14.25 s, 1588×1080 recording (zoomed-in browser) of the "Offloop" site's Product mega-menu. It has a frosted-glass dropdown with a feature list on the left (Flow, Botmode, Channels, Connectors, Agent Memory, Teammates) and a large preview pane on the right that changes on hover. Behind it is a cinematic video of VR-headset audiences shifting from blue to orange.
- **Why it's remarkable:** The menu has no fixed colour. It is translucent, so its tint is borrowed from the hero video (navy, then rust, then near-black, then mauve). Each item gets a bespoke mini-illustration (an avatar-merge diagram, an integrations grid), not just a text blurb.

## 2. Composition & layout
- **Nav bar:** at y≈87 in the zoomed frame, left-aligned items with ~90 px spacing, then a translate icon and a pill "Sign in" (about 158×72 px in zoomed px).
- **Dropdown:** spans x≈60→1558 with an outer radius of about 32 px. It is split about 35/65:
  - **Left column:** a "Features" eyebrow (grey) plus six items at a 77 px pitch.
  - **Right pane:** an inner glass panel, inset ~16 px, radius about 24 px, holding a title, a 2-line description and an illustration area.
- **Final frame (13.46 s):** the true scale. The menu is about 300 px wide at the top-right of the page, and the hero is a centred serif headline "Scale your team's work without scaling headcount" with an email field and a "Join the waitlist →" pill.

## 3. Typography
- **Menu:** Inter-like neo-grotesk. Items are medium at about 32 px zoomed (≈15 px real) in white. The "Features" eyebrow and description are regular in a warm grey.
- **Preview:** the title is medium about 34 px zoomed and the description regular at 1.4 leading.
- **Page hero:** a condensed editorial serif (Instrument Serif-like) at about 40 px real, which contrasts with the sans UI.

## 4. Colour
| Hex | Role | Share (key frame, orange phase) |
|---|---|---|
| #3b1a11 / #51301a | glass panel tinted by the video | 51% |
| #6f4a1c | left column glass (warmer) | 15% |
| #e28129 / #cd672c | backlight glare in video | 10% |
| #96381d / #aa3b1a | nav-bar video zone | 8% |
| #0a0f12 | dark phase (5.54 s) | — |
| #ffffff | item text, title | small |
| mint #6fe0b0 (sampled visually) | memory "node" orb | <1% |

WCAG checks:
- White items on the panel are 15.65:1 (#3b1a11) and 11.75:1 (#51301a).
- Description grey #a8877a on #2e1a12 is 5.04:1.
- Inactive nav links (about #e0a890) on the orange video #96381d are **3.53:1**. They fail at 15 px, and they would vary with the video.
- In the dark phase, grey on #0a0f12 is 5.58:1.

## 5. Depth & material
- **Two tiers of glass:** the outer panel uses a heavy backdrop blur (≈40 px) with about 55% dark tint, and the inner preview panel is darker (about 70%) with a faint 1 px light top edge. The nested glass gives a clear foreground and background within one popover.
- **Active row:** a lighter pill fill (about rgba(255,255,255,.1), radius about 16 px).
- **Icon tiles in Connectors:** about 60 px squircles with about 16 px radius, each a soft dark glass with the logo in white or brand colour. Some cells are left empty and faint, giving a scattered, organic grid.

## 6. Components & patterns
- **Mega-menu with hover preview:** a list on the left and a live preview on the right.
- **Active indicator:** a "→" arrow that slides in before the label, pushing it about 20 px right, plus the pill highlight.
- **Preview illustrations:**
  - Agent Memory: three avatar rows with skeleton lines whose curves converge on a mint orb, then two output lines;
  - Connectors: a 4×3 grid of logos (Notion, GitHub, a bolt, Vercel-style triangle, GitLab and others);
  - Flow: text first, illustration loading.
- Translate icon button and a pill "Sign in".

## 7. Motion
Measured: 14.25 s at 60 fps, 9 segments, motion fraction 0.23, not a loop.

| Segment | Duration | Shape (peak_at) | What happens |
|---|---|---|---|
| 0.30–0.97 s | 0.67 s | symmetric (0.53) | menu opens: blur and scale-in, items deblur (frame 0.79 s shows soft text) |
| 2.57–2.77 s, 3.07–3.23 s | 0.2 / 0.17 s | — | quick hover hops between items |
| 3.50–4.07 s | 0.57 s | symmetric (0.38) | preview change to Flow; the title arrives first and the illustration later |
| 4.17–4.33 s | 0.17 s | ease-out | — |
| 6.13–6.87 s | 0.73 s | ease-out (0.02, instant start) | video cut / colour shift to orange plus the Agent Memory diagram drawing in |
| 12.73–13.43 s | 0.7 s | symmetric (0.45) | zoom-out to the full page |

Content transitions inside the preview pane crossfade with a slight blur, about 0.2–0.3 s estimated from frames 8.71 s (empty) and 10.29 s (grid present).

## 8. Brand system
n/a — not a brand system. Identity cues for "Offloop": cinematic VR-crowd photography with dramatic stage lighting, an editorial serif hero against sans UI, and mint as the AI "node" accent.

## 9. UX
- **Strengths:** Hover previews explain features before the click; there is a clear active state (arrow plus fill); the grid conveys "many integrations" instantly.
- **Risks:**
  - The preview illustrations appear after a delay (one frame shows an empty pane), which could feel laggy.
  - Translucency makes text contrast depend on the video frame.
  - On touch devices, hover previews need a tap-to-preview fallback.

## 10. Craft signals
- The nested glass panels have the outer radius (about 32 px) equal to the inner radius (about 24 px) plus the inset (≈8–16 px), roughly concentric.
- The active row's arrow animates in and shifts the label, not just a colour change.
- The panel tint is inherited live from the moving video behind it (blue, rust, black and mauve phases all visible).
- The integration grid leaves deliberate empty cells for an irregular, airy rhythm.
- Illustrations use skeleton lines (no fake copy), keeping the preview abstract and on-brand.
- The serif hero versus the sans navigation is a clean two-family system.

## 11. Reproduction recipe
```css
:root{--glass:rgba(20,12,8,.55);--glass-in:rgba(10,6,4,.45);--hi:rgba(255,255,255,.10);
  --text:#fff;--mute:rgba(255,255,255,.55);--r-out:32px;--r-in:24px;--r-row:16px}
.mega{display:grid;grid-template-columns:35% 1fr;gap:16px;padding:16px;border-radius:var(--r-out);
  background:var(--glass);backdrop-filter:blur(40px) saturate(140%);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 30px 60px rgba(0,0,0,.35);
  transform-origin:top left;animation:open .67s cubic-bezier(.45,0,.55,1) both}
@keyframes open{from{opacity:0;filter:blur(8px);transform:scale(.97)}}
.mega li a{display:flex;gap:8px;padding:10px 16px;border-radius:var(--r-row);font:500 15px "Inter";color:var(--text)}
.mega li a::before{content:"→";width:0;opacity:0;transition:width .2s,opacity .2s}
.mega li a:hover{background:var(--hi)}
.mega li a:hover::before{width:16px;opacity:1}
.preview{border-radius:var(--r-in);background:var(--glass-in);padding:24px}
.preview>*{animation:in .3s ease-out both}
.preview .art{animation-delay:.12s}
@keyframes in{from{opacity:0;filter:blur(6px)}}
.hero h1{font:400 64px/1.05 "Instrument Serif",serif}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 9 | Cinematic backdrop, nested glass and tasteful illustrations; the colour shifts make it alive. |
| Originality | 7 | Hover-preview mega-menus are known; the video-tinted glass and diagram previews refresh it. |
| Usability | 8 | Clear states and informative previews; contrast depends on the video and touch needs care. |
| Craft | 8 | Concentric radii, staggered preview reveals and a consistent arrow indicator. |
