---
id: bg-reddit
source: brandguidelines
category: guideline
status: analyzed
title: "Reddit Brand System (Lingo-hosted)"
creator: "Reddit, Inc. (hosted on Lingo DAM)"
styles: [corporate-clean, playful-rounded, minimal-swiss]
patterns: [conversation-bubble-as-core-shape, lingo-sidebar-kit-template, version-switcher-with-legacy-banner, mission-description-positioning-triplet, kit-with-14-chapters, orange-hero-wordmark-panel]
mode: light
palette: ["#ff4500", "#242425", "#000000", "#ffffff", "#e1e2e4", "#a3a4a6", "#3769e4", "#6066e3"]
type_families: ["Reddit Sans (400/400i/600/800, host UI + brand)", "Inter (Lingo chrome, loaded)", "Source Code Pro (in CSS only)"]
type_class: [geometric-sans, humanist-sans]
radius_px: [4, 6, 20]
motion: {durations_s: [0.3, 0.2, 0.1, 0.4], easing: [ease, ease-in-out, "cubic-bezier(0.02,0.22,0.55,1)"], loop: false}
scores: {aesthetics: 6, originality: 6, usability: 6, craft: 6}
craft_signals: [orange-hero-block-full-bleed, bubble-in-wordmark-counters, consistent-14px-24px-body-rhythm, hairline-1px-e1e2e4-dividers, mobile-pager-1-of-14]
anti_patterns: [capture-shows-only-overview-chapter, duplicated-sidebar-in-capture, legacy-version-banner-in-blue, default-host-chrome-dilutes-brand]
---
# Reddit Brand System (Lingo-hosted) — Reddit, Inc.

## 1. Snapshot
- **Subject:** Reddit's brand hub on the Lingo digital-asset platform. `site_meta.json` shows the requested kit URL (`reddit.lingoapp.com/s/orqY1E/?v=19`) redirected to `/k/Brand-foundation-oYYL4W`; no Wayback archive. The capture is only the "Overview / Brand foundation" chapter. The hub lists 14 chapters (mobile pager reads "1 of 14"). A second capture shows an older "v5.1" version of the same page, and the live page carries a "Legacy version" banner.
- **Why it's remarkable:** The whole identity is explained through one idea, the "conversation bubble". It sits inside the wordmark counters and is also used as a shape-shifting container for headlines. The captured page is thin. I only saw the foundation chapter, so the claims below about logo, colour and motion rules are limited to the chapter titles and what the foundation page states.

## 2. Composition & layout
- Fixed top bar 72 px tall: Snoo avatar, "Reddit Brand Resources / Brand foundation" breadcrumb (grey `#a3a4a6` then black), and a search field at right (about 200 px wide, 4 px radius).
- A 240 px left sidebar lists the chapters: Overview (with Strategic and Visual foundation as sub-items), Traits & values, Snoo, Logo, Conversation Bubble, Typography, Color, Illustration, Photography, Composition, Motion principles, Voice & tone, Displaying content, General rules. The v5.1 build uses Brand values, Social, Reddit rules and Resources instead.
- Content column about 816 px (x≈427–1243) centred in the remaining space, with a 1 px `#e1e2e4` right edge. The hero panel is a full-width orange block 816×460.
- Mobile (390 px): header collapses to logo plus title and a search/menu pair; sidebar becomes a bottom pager ("1 of 14" and a "Traits & values" next link). Orange hero scales to a 310 px block.

## 3. Typography
Computed styles from `census_home.json` show a single family, Reddit Sans, at 229 of 229 text nodes.

| Role | Spec |
|---|---|
| Page title | 36 / 56, weight 900 |
| Section title | 28 / 40, weight 600 |
| Lead paragraph | 22 / 32, weight 600 |
| Body | 14 / 24, weight 400 (83 of 113 nodes) |
| Label | 14 / 24, weight 600 |
| Caption | 12 / 16, weight 400 |

Letter-spacing is `normal` everywhere. Body is small at 14 px but gets a generous 1.71 line-height. Lead copy is set heavier (600) rather than larger, which gives a clear two-level read inside long text.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #ffffff | page, panels | 75–88% of tiles |
| #ff4500 | Reddit orange-red, hero block, active-nav tick, links | 12% on tile 1, 3–7% elsewhere |
| #242425 | body text (33 nodes) | text |
| #000000 | headings and nav (72 nodes) | text |
| #e1e2e4 | dividers, active-nav chip | UI |
| #a3a4a6 | breadcrumb prefix, footer links | UI |
| #3769e4 | "Legacy version" banner (Lingo chrome) | UI |
| #6066e3 | Lingo footer link | UI |

Contrast: #242425 on white **15.51:1**; #ff4500 on white **3.44:1** (fails AA for body text, passes large); #a3a4a6 on white **2.49:1** (fails; used for the breadcrumb prefix and footer). Reddit orange is therefore used for a block and for a "next" link (about 16 px, 3.44:1 is marginal).

## 5. Depth & material
Flat. The only shadows are host-UI: `0 1px 3px rgba(36,36,37,.12)` on small controls and a 12 px blur dropdown shadow. Brand artwork has no gradients. The key graphic (orange speech-bubble headline) is flat colour with black type.

## 6. Components & patterns
- Sidebar tree with an orange 2 px left tick for the active item and a grey `#e1e2e4` chip for the active parent.
- A blue "Legacy version" button with an info icon above the nav, plus a version dropdown (v2.01, v5.1).
- Statement block: a heading in the 22/32 semi-bold above a 14 px paragraph. Mission, Description and Positioning are shown as a labelled triplet (small label, larger statement).
- Orange hero panel with white Snoo and the "reddit" wordmark. A second demonstration is the "Reddit is all about conversation" bubble: three lines of black Reddit Sans in an orange chat shape with a tail at bottom left.
- The video block (black grid background, 816×460) has a centred play affordance.

## 7. Motion
Host transitions are `all 0.3s ease` (206 uses), `opacity 0.3s ease`, `color 0.3s ease`, `opacity 0.1s ease-in-out` on hover, and a single `width 0.2s cubic-bezier(0.02,0.22,0.55,1)` (an ease-out) on search. The brand page names a "Motion principles" chapter that is not in the capture, and the v5.1 page embeds an animated bubble video.

## 8. Brand system
This is the main section, but the capture gives only the foundation chapter.
- **Strategic foundation (stated):** mission "Bring community, belonging, and empowerment to everyone" in v2.01, and "To empower communities, and make their knowledge accessible to everyone" in v5.1. Description: "Reddit is the heart of the internet." Positioning: "Where we discover and participate through real conversation."
- **Visual foundation (stated):** "energetic and approachable"; the **conversation bubble** is the core of the identity. It is found nested in the counters of the wordmark, in the lowercase letters of Reddit Display, and used as a shape-shifting graphic component for any aspect ratio.
- **Chapters (v2.01 order):** Overview, Traits & values, Snoo, Logo, Conversation Bubble, Typography, Color, Illustration, Photography, Composition, Motion principles, Voice & tone, Displaying content, General rules.
- **Governance:** all commercial use is reserved to Reddit and licensed partners; elements must come from the kit, not third-party sources. It describes itself as "living".
- **Not verifiable here:** logo clearspace, minimum size, exact palette beyond #ff4500, and type scale rules are inside other chapters I did not see.

## 9. UX
Persistent searchable chapter nav, versioning with an explicit legacy warning, deep links per chapter. Weaknesses: the generic Lingo shell (blue banner, Inter UI, grey footers) adds a second visual voice. The capture duplicates the sidebar down the page, which suggests a sticky element that re-renders per tile.

## 10. Craft signals
- Single type family used from 12 px to 36 px with a fixed 24 px body leading.
- The foundation hero uses a single flat colour (#ff4500) edge to edge.
- 1 px #e1e2e4 hairlines on header, sidebar and footer rule.
- The bubble headline reuses the logo's shape language so the graphic and the wordmark rhyme.
- Mobile pager shows position ("1 of 14").

## 11. Reproduction recipe
```css
:root{--reddit-orange:#ff4500;--ink:#242425;--rule:#e1e2e4;--mute:#a3a4a6;--font:"Reddit Sans",system-ui,sans-serif}
body{font:400 14px/24px var(--font);color:var(--ink);background:#fff}
h1{font:900 36px/56px var(--font)} h2{font:600 28px/40px var(--font)}
.lead{font:600 22px/32px var(--font);color:#000}
.hero{background:var(--reddit-orange);aspect-ratio:816/460;display:grid;place-items:center}
.bubble{background:var(--reddit-orange);color:#000;font:800 48px/1 var(--font);
  padding:.4em .8em;border-radius:48px 48px 48px 6px}
.nav a{transition:color .3s ease,opacity .3s ease}
.nav a[aria-current]{border-left:2px solid var(--reddit-orange)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 6 | Strong orange hero and bubble, but the host chrome is generic. |
| Originality | 6 | The bubble-in-wordmark idea is distinctive; the kit format is standard Lingo. |
| Usability | 6 | Clear nav and versions, but only one chapter visible in the capture. |
| Craft | 6 | Consistent type rhythm and hairlines; contrast of orange and grey text is weak. |
