# Audit: file:///home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-1/B/outputs/index.html

**Hard gates:** FAIL → contrast, focusVisible, minTextSize

- ✗ contrast: {"fails":1,"note":"text over background-images is listed but must be verified visually"}
- ✓ noOverflow390: {"overflowPx":0}
- ✗ focusVisible: {"stops":12,"invisible":["a:See how it works","a:Start free trial"]}
- ✓ reducedMotion: {"normal":6,"reduced":0,"hasMediaQuery":true}
- ✗ minTextSize: {"tiny":[{"text":"Tue 8:00","size":10},{"text":"Tue 8:04","size":10},{"text":"Cadence read intent: reschedule · aftern","size":11},{"text":"Tue 8:04","size":10},{"text":"Tue 8:05","size":10},{"text":"Tue 8:05","size":10},{"text":"Dr. Patel","size":11},{"text":"Dr. Kim","size":11},{"text":"N.P. Ortiz
- ✓ altAndNames: {"imgsWithoutAlt":0,"unnamedControls":[]}

**Warnings:**
- 5 touch targets < 44px at 390px
- 1 heading level skips
- 10 distinct radii: 3, 10, 16, 18, 24, 28, 32, 36, 44, 999 (aim for 2-3 + pill)
- 3 saturated hue families (aim for 1 accent unless colour-coding categories)

**Worst contrast pairs:**
- 3.01:1 (needs 4.5) #9fc8c5 on #0f766e 10px "Tue 8:04" <time>

Fonts: Inter, Instrument Serif, JetBrains Mono | radii: 3, 10, 16, 18, 24, 28, 32, 36, 44, 999

Screenshots: /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-1/B/audit_final/shot-390.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-1/B/audit_final/shot-768.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-1/B/audit_final/shot-1440.png, /home/user/design-master/skills/aaa-design-workspace/iteration-2/eval-1/B/audit_final/shot-1440-reduced.png