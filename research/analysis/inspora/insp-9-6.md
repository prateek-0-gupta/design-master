---
id: insp-9-6
source: inspora
category: Motion
status: analyzed
title: "tabs animation"
creator: "@marcelkargul"
styles: [dark-premium, micro-interaction, monochrome, hairline-ui]
patterns: [tab-bar, active-underline-indicator, spotlight-glow-below-tab, inner-bottom-glow, icon-plus-label-tab, filled-icon-active-state]
mode: dark
palette: ["#0f0f0f", "#1a1a1a", "#292929", "#565656", "#8c8c8c", "#ffffff"]
type_families: ["Geist / Inter Display-style neo-grotesk (likely)"]
type_class: [neo-grotesk]
radius_px: [12]
motion: {durations_s: [0.5, 2.0, 5.97], easing: [ease-in-out], loop: true}
scores: {aesthetics: 8, originality: 6, usability: 7, craft: 8}
craft_signals: [underline-sits-on-divider-hairline, glow-cone-falls-below-divider, inner-bottom-rim-light-on-active-tab, underline-grows-from-centre, icon-fill-switches-to-white, inactive-tab-keeps-surface]
anti_patterns: [glow-low-energy-subtle, divider-nearly-invisible]
---
# tabs animation — @marcelkargul

## 1. Snapshot
- **Subject:** A 5.97 s, 1920×1728 loop of a two-tab switcher, "Emails" and "Attachments", on near-black. The active tab lights up like a lamp: a white underline appears on the divider and a soft cone of light spills downward into the content area.
- **Why it's remarkable:** The active indicator is treated as a light source rather than a coloured bar. Selection reads as "this tab is illuminating the panel below", a physical metaphor carried entirely in greyscale.

## 2. Composition & layout
- Two tabs are centred at y≈835 in the key frame, sitting on a full-width 1–2 px divider at y≈970.
- **Tab sizes:** about 450×160 px (Emails) and about 675×160 px (Attachments), with a gap of about 70 px. Inside each, an icon of about 80 px and the label have a 40 px gap. At 1× (÷3.2) this is roughly a 50 px-tall tab with 13 px padding and 15–16 px text.
- Everything above and below is empty #0f0f0f. The cone of light is the only element in the content zone.

## 3. Typography
- A neo-grotesk with a double-storey "a", flat-terminal "s" and straight-cut "t", closest to Geist or Inter Display. It is about 88 px at capture (about 17 px at 1×), Medium weight, with no visible tracking adjustment.
- **States:** active text is pure white and inactive text is about #8c8c8c. There is no weight change between states, so width stays stable and nothing reflows.

## 4. Colour
| Hex | Role | Approx share |
|---|---|---|
| #0f0f0f | canvas | 98.6% |
| #1a1a1a | tab surface | 0.4% |
| #292929 / #343434 | tab rim, divider | 0.2% |
| #565656 / #6e6e6e | inactive icon fill, glow mid-tones | 0.6% |
| #8c8c8c | inactive label | — |
| #ffffff | active label, icon and underline | <0.2% |

WCAG checks:
- Inactive label #8c8c8c on #1a1a1a is 5.18:1 (pass).
- Active white on #1f1f1f is 16.48:1.
- The divider and glow edge (#6e6e6e on #0f0f0f, 3.76:1) are decorative only.

## 5. Depth & material
- **Tabs:** #1a1a1a slabs with a radius of about 36 px at capture (about 12 px at 1×) and a 1 px slightly lighter top rim.
- **Active tab gets two lights:**
  1. An inner bottom glow, a radial white bloom inside the tab's lower edge, as if lit from underneath.
  2. An external light cone, a big elliptical radial gradient (about 900×700 px at capture) below the divider, fading from about #2a2a2a to the canvas.
- The underline is a 6–8 px (about 2 px at 1×) white bar with rounded ends, sitting exactly on the divider line.

## 6. Components & patterns
- Segmented tabs with icon and label. Icons are filled glyphs (inbox tray, paperclip). The active icon turns white and the inactive one stays grey.
- The underline indicator matches the tab width minus about 4 px.
- The inactive tab keeps its #1a1a1a pill, so both tabs always look tappable. Only light distinguishes the active one.

## 7. Motion
- **Measured:** 5.97 s at 30 fps with motion fraction **0.01**. No segment crosses the energy threshold (0.35) and p95 energy is 0.26: all transitions are slow, low-contrast fades. First/last diff is 0.03 and `seamless_loop_likely: true`.
- **From the frames (estimates):**
  - Emails lights at about 0.6–1.0 s, holds to about 2.0 s, then its underline **shrinks toward centre** (2.32 s shows a short ~75 px bar) and the glow fades.
  - At about 3.0 s nothing is lit.
  - Attachments then lights in the same way at about 3.3–3.65 s, holds, and decays at about 4.97 s, when the underline is again shorter and centred.
- **Inferred timing:** each on and off transition lasts about 0.4–0.6 s, ease-in-out, with the underline scaling on X from the centre. The cone and the inner glow fade in sync with it.

## 8. Brand system
n/a — not a brand system. The cue is a "light as state" language suited to a premium dark mail client.

## 9. UX
- State is communicated three ways: label brightness, a filled white icon and the underline plus glow. That is robust even if the glow is invisible on poor displays.
- Both tabs keep the same surface, so the hit area is obvious.
- The demo shows a dark "all-off" moment between tabs (about 3 s). In product, the indicator should slide or hand off directly rather than going through an empty state.
- The glow is so subtle (about 6% luminance lift) that on low-quality panels it may vanish. The underline carries the real signal.

## 10. Craft signals
- The underline sits on the divider hairline rather than under the tab, so the tab "plugs into" the panel below.
- The glow cone starts at the divider and extends only downward: light falls into the content, never up into empty space.
- An inner bottom rim light on the active tab shows the same light leaking upward through the tab.
- The underline animates from the centre outward and back.
- There is no weight change on activation, so there is zero layout shift.
- Icon style flips from grey fill to white fill, the same glyph set at the same size.

## 11. Reproduction recipe
```css
:root{--bg:#0f0f0f;--tab:#1a1a1a;--rim:#292929;--muted:#8c8c8c;--on:#fff;--r:12px;
  --font:"Geist","Inter",system-ui,sans-serif;--ease:cubic-bezier(.65,0,.35,1)}
.tabs{display:flex;gap:20px;justify-content:center;border-bottom:1px solid #1c1c1c;padding-bottom:14px;position:relative}
.tab{position:relative;display:flex;gap:12px;align-items:center;padding:12px 14px;border-radius:var(--r);
  background:var(--tab);box-shadow:inset 0 1px 0 var(--rim);color:var(--muted);font:500 17px/1 var(--font);
  transition:color .5s var(--ease)}
.tab::before{content:"";position:absolute;inset:auto 10% 0;height:60%;border-radius:inherit;opacity:0;
  background:radial-gradient(60% 100% at 50% 100%,rgba(255,255,255,.35),transparent);transition:opacity .5s var(--ease)}
.tab::after{content:"";position:absolute;left:0;right:0;bottom:-15px;height:2px;border-radius:2px;background:var(--on);
  transform:scaleX(0);transition:transform .5s var(--ease)}
.tab[aria-selected=true]{color:var(--on)}
.tab[aria-selected=true]::before{opacity:1}
.tab[aria-selected=true]::after{transform:scaleX(1);
  box-shadow:0 0 12px 2px rgba(255,255,255,.35), 0 120px 160px 60px rgba(255,255,255,.06)}
```

## 12. Rating
| Axis | Score | Why |
|---|---|---|
| Aesthetics | 8 | Pure greyscale with one light source. Restrained and premium. |
| Originality | 6 | Glow underlines are trending. The downward cone into the panel is the distinguishing touch. |
| Usability | 7 | Triple-encoded state with good label contrast. The all-off gap in the demo would be confusing in product. |
| Craft | 8 | Divider alignment, no layout shift, and centre-out scaling are carefully done. |
