# aaa-design: the site

`index.html` is the page about the skill, built with the skill itself. Open it directly in a browser; it's self-contained apart from Google Fonts.

- **Reasons layer:** press **R**, use the header toggle, or open `index.html?reasons` to annotate every design decision with its rule and the evidence behind it.
- **Hero data:** the 347 squares are the real worst-contrast ratios from `research/analysis/*` §4, inlined in the page and also stored in `data/contrast.json`.
- **Use cases:** `usecases/*/with.html` and `usecases/*/without.html` are the unedited blind-tested builds from `skills/aaa-design-workspace/iteration-2`. Scores are in `data/evals.json`.
- **Audit:** `node ../skills/aaa-design/scripts/audit.mjs index.html ./audit` passes all six hard gates.
