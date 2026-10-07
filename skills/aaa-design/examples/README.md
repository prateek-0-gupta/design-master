# Reference implementations

Each example is a single self-contained HTML file. All of them pass every hard gate in `scripts/audit.mjs` at 390, 768 and 1440 px. The comment at the top of each file states its direction: one structural base plus one expressive layer. Open the closest one before building, to calibrate the bar, but don't copy it.

| File | Base + layer | Shows |
|---|---|---|
| `01-swiss-physical-landing.html` | Neutral Swiss + physical metaphor | Landing hero with a receipt that prints the real line items when you press the CTA; tray-and-card nesting with nested radii; tabular metrics with dimmed units; mono eyebrow; mobile nav collapse |
| `02-dark-agent-console.html` | Dark Premium + state orb | Orb whose shape encodes agent state; one hue per tool threaded through bar, legend and rows; a data table with status pills (colour + word); designed empty filter state; toast with Undo; Esc and keyboard support |
| `03-editorial-brand-page.html` | Editorial Warm + type-as-image | Brand-page anatomy: numbered chapters, each with rule, then mono spec, then proof; swatches showing computed contrast and AA/AAA badges with copy-to-clipboard; live type scale; logo clearspace and a don'ts grid |

Re-run the audit after editing:

```bash
node ../scripts/audit.mjs 02-dark-agent-console.html ./audit
```
