# Audit: file:///home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/A/outputs/index.html

**Hard gates:** FAIL → contrast, minTextSize

- ✗ contrast: {"fails":6,"note":"text over background-images is listed but must be verified visually"}
- ✓ noOverflow390: {"overflowPx":0}
- ✓ focusVisible: {"stops":12,"invisible":[]}
- ✓ reducedMotion: {"normal":0,"reduced":0,"hasMediaQuery":false}
- ✗ minTextSize: {"tiny":[{"text":"HUILA · COLOMBIA","size":6.5},{"text":"red plum · jasmine","size":9},{"text":"WHOLE BEAN · 250 G","size":7},{"text":"COFFEE ROASTERS","size":7},{"text":"TUE – SUN · 8 – 17","size":7}]}
- ✓ altAndNames: {"imgsWithoutAlt":0,"unnamedControls":[]}

**Warnings:**
- 6 touch targets < 44px at 390px
- 5 distinct radii: 10, 14, 16, 18, 99 (aim for 2-3 + pill)
- 4 saturated hue families (aim for 1 accent unless colour-coding categories)
- no @media (prefers-reduced-motion) rule found

**Worst contrast pairs:**
- 1.17:1 (needs 4.5) #ffffff on #f4ecdd 13px "Still life — a cup in side light, steam visible" <span> [over image]
- 3.35:1 (needs 4.5) #c8643b on #f4ecdd 12px "01 — Logo" <div.eyebrow>
- 3.93:1 (needs 4.5) #ffffff on #c8643b 13px "Telha#C8643BRGB 200 100 59 · Accent" <button.sw>
- 3.93:1 (needs 4.5) #ffffff on #c8643b 22px "Telha" <strong>
- 4.18:1 (needs 4.5) #7b6f64 on #f4ecdd 12px "Display / 64" <small>
- 4.22:1 (needs 4.5) #2a1b14 on #c8643b 14px "bom dia." <text>

Fonts: DM Sans, Fraunces | radii: 10, 14, 16, 18, 99

Screenshots: /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/A/audit_final/shot-390.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/A/audit_final/shot-768.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/A/audit_final/shot-1440.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-4/A/audit_final/shot-1440-reduced.png