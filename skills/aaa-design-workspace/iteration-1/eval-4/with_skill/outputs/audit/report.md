# Audit: file:///home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-4/with_skill/outputs/index.html

**Hard gates:** FAIL → contrast, minTextSize

- ✗ contrast: {"fails":1,"note":"text over background-images is listed but must be verified visually"}
- ✓ noOverflow390: {"overflowPx":0}
- ✓ focusVisible: {"stops":12,"invisible":[]}
- ✓ reducedMotion: {"normal":0,"reduced":0,"hasMediaQuery":true}
- ✗ minTextSize: {"tiny":[{"text":"01","size":11},{"text":"02","size":11},{"text":"03","size":11},{"text":"04","size":11},{"text":"05","size":11},{"text":"06","size":11},{"text":"07","size":11},{"text":"08","size":11},{"text":"x","size":11},{"text":"x","size":11}]}
- ✓ altAndNames: {"imgsWithoutAlt":0,"unnamedControls":[]}

**Warnings:**
- 1 touch targets < 44px at 390px
- 4 font families: Inter, Instrument Serif, JetBrains Mono, Arial
- 5 distinct radii: 3, 4, 8, 10, 999 (aim for 2-3 + pill)
- 3 saturated hue families (aim for 1 accent unless colour-coding categories)

**Worst contrast pairs:**
- 4.27:1 (needs 4.5) #b8431a on #ebe3d4 5.2px "Coffee Roasters" <small>

Fonts: Inter, Instrument Serif, JetBrains Mono, Arial | radii: 3, 4, 8, 10, 999

Screenshots: /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-4/with_skill/outputs/audit/shot-390.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-4/with_skill/outputs/audit/shot-768.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-4/with_skill/outputs/audit/shot-1440.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-4/with_skill/outputs/audit/shot-1440-reduced.png