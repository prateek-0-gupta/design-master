# Craft checklist

These details recur in the top-rated quartile (summed score ≥ 32 of 40). Each item is checkable. The ids show where it was observed, and the counts come from `_clusters.json` craft clusters where available. They are grouped so that a final pass can run top to bottom.

## Typography (1–16)

1. Display type carries negative tracking set per size: −0.02em at 40–64px, −0.03em at ≥ 72px (bg-ebay-playbook, bg-klarna, bg-herman-miller; 24 examples).
2. Small caps labels (≤ 13px) are tracked positive, +0.06 to +0.1em (40 examples; insp-support-analytics, bg-klarna +3%).
3. Mono is reserved for metadata, IDs, timings and money. Names and prose stay in sans (57 examples; insp-rag-pipeline, insp-model-router).
4. Numbers use tabular figures and right-align on one edge (`font-variant-numeric: tabular-nums`; insp-4-7, insp-glass-circle-with-a-gradient).
5. Hierarchy comes from size and colour first, weight second, with at most 2 weights per family on a screen (insp-glass-circle, insp-1-41).
6. Display leading is 0.85–1.1, body 1.4–1.55, and they never share one value.
7. Headlines use sentence case; all-caps only for short labels (bg-olympic, bg-new-breed's "loudline" bans all-caps).
8. One expressive move per headline: an italic word, a colour-split second line or a serif swap, not all three (bg-help-scout's heavy sans over a light serif; insp-1-40 splits colour inside a sentence).
9. Numbers in UI copy have units and live readouts ("0.42 µJ"; insp-melon-jelly).
10. Unit symbols and currency are dimmed one step relative to the figure (insp unit-symbol-dimmed).
11. Measure is 60–72ch for prose, enforced with `max-width: 65ch`.
12. Optical alignment: hanging punctuation, and large display type nudged left to the visual edge (bg-discord manually raises commas).
13. Localized strings are budgeted: 10% shorter for EU languages and 15% for Japanese (bg-slack). Character budgets are set per field (bg-spotify: 25/18/23).
14. The verb tense follows state: Create → Creating → Created (insp-1-42).
15. Keyboard hints appear on primary actions ("Approve ↵"; insp-1-30).
16. There are no typos. 20 examples had visible copy errors, and every one lost craft points.

## Colour (17–32)

17. One accent colour per view. Everything else is a neutral ladder (104 examples).
18. Neutrals are tinted: warm off-white instead of #fff (45 examples) and a tinted near-black instead of #000 (30 examples).
19. Dark UIs show elevation by surface tint steps (#000 → #121212 → #1c1c1c → #2a2a2a), not shadows.
20. Every text and background pair is computed, not eyeballed: text-2 ≥ 7:1 and meta ≥ 4.5:1.
21. Text on a brand colour uses a dark ink of the same hue, not white (insp-bento-cards: 5.7–8.0:1 on four pastel cards using `color-mix(in oklab, var(--c) 25%, #000)`).
22. Category colour is threaded through every layer: badge, bar, citation, dot (insp-rag-pipeline, insp-1-48, insp-tracking-cards, insp-coding-agent).
23. The accent appears only where the user is acting (insp-angry-sliders: violet only on the dragged slider).
24. Colour is taken from content: glass is tinted from its wallpaper, the scrim from the photo (78 examples; insp-look-away-preview, insp-3-7).
25. State colour always has a second channel: icon, word or shape (30 examples; insp-wos-island-animations).
26. A deep "ink" variant of each semantic colour exists for text: green #137a3a, not #16a34a on light grey.
27. Gradients have a locked stop order and named presets (bg-new-breed, bg-kazam "90% Pocus to 10% Pixie").
28. Grain at 2–6% on large gradients to kill banding (26 examples; insp-stamp-shader).
29. Chromatic fringe or dispersion is confined to rims, never over text (19 examples; insp-9-8, insp-1-12).
30. Light and dark accents are retuned separately: #3d3dd6 → #4f6ef7 on dark (insp-1-61).
31. The proportion of each colour is stated (60/30/10: bg-hulu, bg-lassomd, bg-help-scout; Kia: primary ≥ 80%, red ≤ 50%).
32. Hues that look like links are not used for non-links.

## Layout and shape (33–48)

33. Two or three radii in total. Nested radius = outer − padding (65 examples; insp-1-30 tray 40 / card 28).
34. Pills for actions and chips, a card radius for containers, 0px for "paper" and media that should feel physical (insp-tap-get-invoice).
35. 1px hairlines at 6–12% ink for structure. Never use a 1px line as the only carrier of information (93 examples).
36. Nesting a card in a tray (a #f2f2f2 tray holding a white card with a 20px inset) groups content without borders (insp-1-30/44/48/58).
37. Grids are visible where they help: crop marks, dimension call-outs and dashed guides (45 examples; insp-ticket-stub, insp-hairlines-v2).
38. Indicators are made from ticks and dots so position reads without labels: ruler sliders, tick progress (74 examples; insp-4-1, insp-folder-icon-timeline).
39. Spacing is proportional to the frame where possible (EDP height ÷ 40, Hulu shortest edge ÷ 6, Olympic's 8px grid table).
40. Controls follow their container's geometry: a tab bends around the window corner, a toggle runs along the card radius (insp-1-52, insp-1-16).
41. A device or browser frame is consistent across a set of screenshots (1042 Studio, Framer).
42. The hero object sits off-centre on a 12-column grid unless the brand is symmetric.
43. Empty space is a deliberate ratio. Top work keeps 30–45% of a hero empty.
44. Layout never shifts when state changes: excluded rows stay dimmed (insp-1-51), fixed-width counters (insp-dynamic-island-streak), the loader shares the result's geometry (insp-1-46).
45. Iconography matches the type stroke (Red Hat: 1.25pt strokes on a 30px grid with 1px overshoot; Kazam: the mark's stroke weight) (75 examples).
46. Pixel art, dither and ASCII snap to a single cell size shared by icons and scene (insp-dynamic-island-pixel-art-horse).
47. Mobile breakpoint content is redesigned, not shrunk. Fixed sidebars must collapse (bg-seat-geek breaks mid-word on mobile).
48. Text sits on a solid zone, never on moving imagery (insp-train-animation footers 10.9–17.4:1 vs insp-interactive-footer 2.26:1).

## Depth and material (49–60)

49. A 1px inner top highlight on raised surfaces: `inset 0 1px 0 rgb(255 255 255/.08)` on dark, `/.6` on light (119 examples).
50. Shadows are tinted with the object's hue or the scene light, not grey-black (86 examples; insp-5-7, insp-6-3).
51. Material shading uses a darker shade of the same hue (insp-2-4 #17852f under #2bc955; insp-3-3 #fcd3c2 → #e3a587).
52. A single light direction across all objects on a screen.
53. Glass = backdrop-blur 16–40px + 1px rim at 20–40% white + tint from the backdrop + noise. Body copy never goes on glass.
54. Ambient-occlusion shadows are layered: a tight contact shadow plus a wide soft one.
55. The physical metaphor has its real behaviour: perforation, tear, spring, gravity (insp-ticket-stub, insp-downloading-an-invoice).
56. The real optical values are exposed when simulating optics (insp-9-8: refraction index 1.52).
57. 3D renders and UI share the palette; the backdrop matches the object (insp-glass-circle).
58. The unlit or off state is visible: unlit LED dots, a slot shadow (insp-airport-matrix-time, insp-boarding-pass-printer).
59. Selection is shown by pushing others back (opacity 0.3, blur 6px) instead of adding a frame (insp-collection-layout).
60. One expressive material per screen.

## Motion (61–74)

61. Duration tokens: 120 / 200 / 320 / 560 / 900ms. Measured median 0.33s.
62. Default ease-out `cubic-bezier(.2,.8,.2,1)`; ease-in only for exits and falls; linear only for machines.
63. Open slower than close, by about 1.5–3×.
64. Content inside a morphing container arrives after it: blur(6px), opacity 0, scale .97 → rest, with a 60–100ms delay.
65. Staggering of 40–80ms per item for lists; the total stays under 400ms.
66. Shared-element continuity: the thing you tapped becomes the thing you see (insp-pill-buttons, insp-morphing-nav, insp-1-41).
67. Every animation communicates state. Constant decorative loops are an anti-pattern (22 examples).
68. Ambient loops are seamless (45% of clips achieve this) and slow, at 3–6s or more.
69. Physics springs are tuned to settle in ≤ 0.6s for UI and ≤ 4s for ornaments (insp-personal-site's 8.1s swing intrudes).
70. Thinking or loading states use slow, non-snapping motion plus staged status text (insp-1-26, insp-5-8).
71. `prefers-reduced-motion` replaces movement with an opacity crossfade of ≤ 150ms. No reference implemented this visibly.
72. Feedback for press arrives at ≤ 100ms (scale .97 or a 1–2px y-shift).
73. Numbers roll or tick rather than jump (insp-5-2, insp-6-7) with tabular figures, so width is stable.
74. Hover and focus states are distinct and can co-exist (insp-8-0: hover fill at 1.43:1, focus is a separate 2px ring offset 4px).

## Content and UX (75–86)

75. Confirmation states show the data itself (stamp prints the date; field becomes the country; receipt prints items).
76. Undo instead of confirm dialogs for reversible destructive actions (insp-paid-stamp, insp-7-6).
77. Progress is shown in more than one synchronized way: bar, stepper and list with times (insp-deploy-pipeline).
78. Inline coaching appears at each step of a gesture (insp-1-60 tooltip copy changes).
79. Controls double as legends (insp-8-9 tinted slider track; insp-time-zones meaning labels).
80. Destinations show their contents (insp-photo-folders peeking photos).
81. Error, empty and 404 states get the same craft as the hero (only 4 examples covered them; this is a gap).
82. Each rule ships its asset: a download beside the rule (bg-channel-4, bg-miro), click-to-copy HEX/RGB/CMYK/PMS (bg-night-embassy).
83. Brand docs give minimum sizes in px and mm, clearspace from the mark's anatomy, and misuse examples.
84. Accessibility tables per colour: an AA/AAA badge on swatches (bg-instacart, bg-mastercard-foundation, bg-firefox).
85. Changelog and version date on living documents (bg-night-embassy).
86. Microcopy has personality but stays specific ("Auto Approve in 27s", "Grounded in 3 sources").
