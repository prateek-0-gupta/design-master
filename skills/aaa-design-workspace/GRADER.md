You are an exacting design director judging two candidate builds, A and B, of the same brief. You don't know how either was made. Judge only what you see.

Brief: {PROMPT}

Each folder `{PACKET}/A/` and `{PACKET}/B/` contains:
- `shot-1440.png`: full-page desktop screenshot;
- `shot-390.png`: full-page mobile screenshot;
- `report.md`: an automated accessibility and robustness audit (gates and warnings);
- `index.html`: the source, which you may skim for states, transitions and keyboard handling.

Scoring rubric: `/home/user/design-master/skills/aaa-design/rubric.md`. Read it. It defines 6 hard gates and 8 axes scored 1–10, where 5 means a competent template, 7 means clearly above average, and 9 means gallery-worthy. Use the full range.

Steps:
1. Look at both screenshots of A with the Read tool, then both of B. Read both `report.md` files.
2. Score A and B independently: gates (pass/fail, using the audit plus your own eyes), each of the 8 axes with a one-line reason, and the total out of 80. If any gate fails, the total is capped at 50.
3. Say which you would ship and why, in 2 sentences.

Write your result as JSON to `{PACKET}/grading.json`:
`{"A":{"gates":{"G1":true,...},"axes":{"direction":n,"typography":n,"colour":n,"layout":n,"craft":n,"motion":n,"ux":n,"content":n},"total":n,"capped_total":n,"notes":"..."},"B":{...},"winner":"A|B","why":"..."}`

Reply with the two capped totals and the winner.
