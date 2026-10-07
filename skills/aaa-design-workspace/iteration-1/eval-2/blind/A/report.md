# Audit: file:///home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-2/A/outputs/index.html

**Hard gates:** FAIL → contrast, noOverflow390, focusVisible, minTextSize

- ✗ contrast: {"fails":2,"note":"text over background-images is listed but must be verified visually"}
- ✗ noOverflow390: {"overflowPx":324}
- ✗ focusVisible: {"stops":12,"invisible":["a:Overview","a:Orders6","a:Inventory","a:Customers","a:Analytics","a:Promotions","a:Settings"]}
- ✓ reducedMotion: {"normal":0,"reduced":0,"hasMediaQuery":true}
- ✗ minTextSize: {"tiny":[{"text":"6","size":11},{"text":"£0k","size":11},{"text":"£1k","size":11},{"text":"£2k","size":11},{"text":"£3k","size":11},{"text":"£4k","size":11},{"text":"8 Sept","size":11},{"text":"14 Sept","size":11},{"text":"20 Sept","size":11},{"text":"26 Sept","size":11}]}
- ✓ altAndNames: {"imgsWithoutAlt":0,"unnamedControls":[]}

**Warnings:**
- 21 touch targets < 44px at 390px
- 6 distinct radii: 7, 8, 9, 10, 14, 99 (aim for 2-3 + pill)
- 3 saturated hue families (aim for 1 accent unless colour-coding categories)

**Worst contrast pairs:**
- 3.58:1 (needs 4.5) #b7791f on #fffdf9 12.5px "Pending" <span.st.pending>
- 4.24:1 (needs 4.5) #7a7367 on #f6f3ee 14px "Wednesday 7 October · here's how Bramble & Co is t" <p>

Fonts: Inter, Fraunces | radii: 7, 8, 9, 10, 14, 99

Screenshots: /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-2/A/audit_final/shot-390.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-2/A/audit_final/shot-768.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-2/A/audit_final/shot-1440.png, /home/user/design-master/skills/aaa-design-workspace/iteration-1/eval-2/A/audit_final/shot-1440-reduced.png