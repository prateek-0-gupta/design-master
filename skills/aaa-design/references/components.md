# Component patterns

Every interactive component ships 8 states: default · hover · focus-visible · active · disabled · loading · error · empty/success. Recipes use the token names from `token-presets.md`.

## Contents
Buttons · Inputs & forms · Segmented control & chips · Toggle & slider · Cards & tray-nesting · Navigation · Tables & lists · Status, progress & AI states · Toasts & undo · Empty / error / 404 · Modals & popovers · Charts & numbers

---

## Buttons
```css
.btn{--h:44px;display:inline-flex;align-items:center;gap:8px;height:var(--h);padding:0 18px;border-radius:var(--radius-pill);
  font:500 15px/1 var(--font-sans);letter-spacing:-.005em;border:1px solid transparent;cursor:pointer;
  transition:background var(--dur-1) var(--ease-out),transform var(--dur-1) var(--ease-out),box-shadow var(--dur-2) var(--ease-out)}
.btn-primary{background:var(--accent);color:var(--on-accent);box-shadow:var(--highlight),0 1px 2px rgb(0 0 0/.12)}
.btn-primary:hover{background:color-mix(in oklab,var(--accent) 88%,#000)}
.btn:active{transform:translateY(1px) scale(.985)}
.btn:focus-visible{box-shadow:var(--focus-ring)}
.btn[disabled]{opacity:.45;cursor:not-allowed}         /* plus aria-disabled for links */
.btn[aria-busy="true"]{color:transparent;position:relative} .btn[aria-busy="true"]::after{content:"";position:absolute;inset:0;margin:auto;width:16px;height:16px;border-radius:50%;border:2px solid var(--on-accent);border-right-color:transparent;animation:spin .7s linear infinite}
.btn-ghost{background:transparent;color:var(--text-1);border-color:var(--hairline)} .btn-ghost:hover{background:var(--surface-2)}
```
Rules:
- **One primary button per view.** A keyboard hint can sit on the primary (`Approve ↵`).
- **The label changes tense with state:** "Deploy" → "Deploying…" → "Deployed".
- **Icon-only buttons get `aria-label`** and a 44px hit area, even if the drawn icon is 20px.

## Inputs & forms
- **Labels:** always visible above the field. Placeholder text is an example, not the label.
- **Height:** 44–48px, with a 1px `--border-control` border (≥ 3:1).
- **Focus:** a ring, plus the border changes to accent-ink.
- **Errors:**
  - text below the field in danger-ink with an icon;
  - `aria-invalid="true"` plus `aria-describedby` pointing at the error text;
  - validate on blur, not on every keystroke.
- **Success** is quiet: a check icon only.
- **Helper text** in text-3 (≥ 4.5:1).
- **Group** related fields. Use one column on mobile.

## Segmented control & chips
```css
.seg{display:inline-flex;padding:4px;gap:2px;background:var(--surface-2);border-radius:var(--radius-pill)}
.seg button{height:36px;padding:0 14px;border-radius:var(--radius-pill);color:var(--text-2);font:500 14px/1 var(--font-sans)}
.seg button[aria-pressed="true"]{background:var(--canvas);color:var(--text-1);box-shadow:var(--shadow-1),var(--highlight)}
```
- Animate a single moving indicator, not each button.
- In a radiogroup, arrow keys move the selection.
- Chips that overflow scroll horizontally, with an edge fade (`mask-image: linear-gradient(90deg,#000 85%,transparent)`) as the overflow cue.

## Toggle & slider
- **Toggle:** a 44×26 track with a 22px thumb. The "on" state uses the accent plus a check glyph inside the thumb, so it isn't colour-only. Thumb travel is `--dur-2` on `--ease-out`.
- **Slider:**
  - put the label and live value in the row (value in tabular figures with dimmed units);
  - put plain-word end labels on the track ("quiet — loud");
  - track contrast ≥ 3:1 against the surface;
  - Reset appears only after a change.

## Cards & tray-nesting
- **Tray-plus-card:** a `--surface-2` tray (radius R) holds a `--canvas` card inset by p, with radius R−p. The tray carries the header, status and actions; the card carries the content. This groups without borders.
- **Card interaction:** hover lifts by 2px plus `--shadow-2` over `--dur-2`. On dark themes, lighten one surface step instead.
- **Selection:**
  - show it by pushing others back (opacity .4, optional blur 4px) or with a 2px accent ring;
  - never by colour alone;
  - keep card height stable between states (dim excluded rows rather than removing them).
- **Bento:** 12-column grid with spans of 4/8/6. One hero tile per grid. Gaps of 16–24px with a radius of 20–28px.

## Navigation
- **Desktop top bar:** 64–72px tall. Logo left, 3–6 links, one primary CTA right. Sticky with blur only if content scrolls under it.
- **Mobile:** collapse to a menu button (44px), opening a full-height sheet with focus trap and Esc to close. Or use a bottom tab bar of 3–5 items with icons plus labels.
- **Sidebar:** 240–280px, with section labels in caps text-3.
  - Active item: an accent bar or dot plus text-1 and weight 500.
  - Hover: a surface-2 fill.
  - Collapses below 1024px.
- **Current page:** mark it with `aria-current="page"`.

## Tables & lists
- **Rows:** 44–56px with a hairline divider.
- **Numbers:** right-aligned and tabular. Units are dimmed. Headers are 12px caps text-3, +0.06em.
- **Row states:** hover `--surface-1`. Selection uses a checkbox plus an `--accent-soft` fill.
- **Overflow:** sticky header; horizontal scroll inside the table on mobile, never the whole page.
- **Empty table:** keep the headers and show an inline empty state.

## Status, progress & AI states
- **Show progress two ways and keep them synced:** a bar plus a stepper or list with per-step times ("Build 42s ✓").
- **Status pill:** dot + word ("● Running"). Colour plus word, never colour alone.
- **AI thinking:**
  - one stable object (orb, dot grid or shape) whose form changes per state (idle, listening, thinking, speaking);
  - staged status text, with a shimmer laid over text that already passes contrast;
  - stream the result into place;
  - cite sources with colour-threaded badges.
- **Skeletons:** match the final layout's geometry exactly. A slow shimmer (1.6s) is fine; respect reduced motion.

## Toasts & undo
- **Position:** bottom-centre on mobile, bottom-right on desktop.
- **Content:** an icon, one line, and an action ("Undo"). Toasts with an action stay 6–8s.
- **Announce:** use `role="status"` / `aria-live="polite"`.
- **Destructive reversible actions:** do them immediately and offer Undo, rather than a confirm dialog.

## Empty / error / 404
The references almost never designed these, which is where you can stand out.
- **Empty:** a small illustration or the page's signature device, the reason it's empty, and one action. Example: "No invoices yet — create your first one" plus a button.
- **Error:**
  - plain language and the cause if it's known;
  - what was preserved ("Your draft is saved");
  - a retry, and a secondary route (contact, or go back);
  - keep the layout chrome.
- **404:** on-brand and helpful, with search, the top 3 destinations and home. The signature motion can appear here, at reduced intensity.

## Modals & popovers
- **Modals:** max-width 480–640px with radius `--radius-2`. The backdrop is rgb(0 0 0/.4) plus a 4px blur.
- **Focus:** trapped inside, starting on the first field or primary action. Esc and a backdrop click close it, and focus returns to the trigger.
- **Animation:** popovers scale from their trigger origin (.96 → 1) over `--dur-3` ease-out, and close over `--dur-2` ease-in.

## Charts & numbers
- **Geometry from data:** 10×10 dot grids for percentages; bars start at zero.
- **Labels:** directly on the series, rather than in a legend, when there are ≤ 4 series.
- **Colour:** series colours ≥ 3:1 against the background. Category hues match the rest of the UI.
- **Big numbers:** tabular, with the unit at 50–60% size in text-2, and the delta with a sign and arrow plus colour.
- **Accessibility:** provide a text summary for screen readers ("Revenue up 12% to $48.2k").

## Visually-hidden content
- Screen-reader-only text and tables (`.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}`) must sit inside a positioned ancestor (`position:relative`).
- Without one, they escape to the page edge and create horizontal overflow at 390px. This bug appeared twice during the skill's own builds. Tables ignore `width:1px`; wrap them in a hidden `div` instead.
