"""Phase 4: map free-form analysis tags to canonical clusters with transparent regex rules, then count
distinct examples per cluster overall and per category (with example ids). -> synthesis/_clusters.json
Rules are ordered; a tag can hit several clusters. Unmatched tags are kept in 'unclustered'."""
import glob, json, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aggregate import front
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

PATTERNS = {
 'pill-and-chip controls (segmented, chips, pill buttons)': r'pill|chip|segment',
 'cards & card stacks / bento': r'card|bento|tile|tray',
 'morphing / expanding container (button→panel, island)': r'morph|expand|grow|island|container|into-',
 'status / progress / step indicators': r'status|progress|step|stepper|timeline|tracker|pipeline',
 'loader / thinking / generating states': r'load|thinking|generat|skeleton|shimmer|spinner|scanning|typing',
 'AI agent / assistant UI': r'\bai\b|ai-|agent|assistant|prompt|chat|voice|llm|copilot',
 'hover / press / selection feedback': r'hover|press|select|active|focus|highlight',
 'toggle / switch / slider / knob controls': r'toggle|switch|slider|knob|dial|ruler|stepper|picker|drum',
 'navigation (tab bar, sidebar, menu, dock)': r'nav|tab|sidebar|menu|dock|rail|breadcrumb',
 'hero / landing sections': r'hero|landing|above-the-fold|headline',
 'footer sections': r'footer',
 'device mockups / product framing': r'mockup|device|phone|browser-frame|window|bezel',
 'glass / blur / frosted surfaces': r'glass|frost|blur|translucent|refract|lens',
 'orb / blob / shader objects': r'orb|blob|shader|liquid|fluid|jelly|metal|chrome|gooey',
 'physical metaphor objects (stamp, receipt, ticket, folder, paper)': r'stamp|receipt|ticket|folder|paper|envelope|cassette|cartridge|printer|sticker|card-stub|boarding|ipod|keycap|lego',
 'data viz / charts / numeric readouts': r'chart|graph|stat|metric|readout|counter|number|delta|kpi|dashboard|dot-matrix|matrix',
 'pixel / dot-matrix / dither / ascii textures': r'pixel|dither|ascii|halftone|dot-grid|led',
 'icon systems & app icons': r'icon|glyph|pictogram|squircle',
 'logo / wordmark / lockup': r'logo|wordmark|lockup|logomark|monogram|clearspace|marque',
 'mascot / character': r'mascot|character|anthropomorph|creature',
 'swatches / palette display': r'swatch|palette',
 'type specimen / editorial type layout': r'specimen|typograph|serif|type-|editorial|kinetic|letter',
 'photo-led / full-bleed imagery': r'photo|image|full-bleed|bleed|imagery',
 'illustration / isometric scenes': r'illustrat|isometric|scene|diorama',
 '3D renders / camera moves': r'3d|render|camera|perspective|tilt|parallax',
 'drag / gesture / direct manipulation': r'drag|swipe|gesture|pull|scrub|throw|fling',
 'toast / confirmation / success / undo': r'toast|confirm|success|undo|done|complete',
 'empty / error / 404 states': r'empty|error|404|offline|not-found',
 'onboarding / sign-up / forms': r'onboard|sign|form|input|field|waitlist|checkout|payment',
 'dark/light theme switching': r'theme|dark-mode|light-dark|day-night|night',
 'carousel / slideshow / reel': r'carousel|slideshow|reel|marquee|scroll',
 'grid & layout guides (crop marks, dashed guides, rulers)': r'grid|guide|crop|ruler|dashed|blueprint|spec',
 'colour-coded categories (one hue per entity)': r'per-|colour-coded|color-coded|hue-|category',
}
CRAFT = {
 'monospace for metadata/labels/numbers': r'mono',
 'tabular / aligned numerals': r'tabular|numeral|aligned-amount|right-aligned',
 'tracked caps micro-labels': r'caps|uppercase|tracked',
 'tight negative tracking on display type': r'negative-track|tight-track|minus|-tracking|tracking',
 'single accent colour, everything else neutral': r'single|one-accent|only|lone|sole',
 'hue-matched / tinted shadows & glows': r'tint|hue-match|colou?red-shadow|glow|coloured',
 '1px hairlines / borders / dividers': r'hairline|1px|divider|rule|stroke|outline|border',
 'inner highlight / rim light / specular edge': r'rim|inner|specular|highlight|edge|bevel|inset',
 'consistent radius system / nested radii': r'radius|corner|concentric|nested|squircle',
 'grain / noise / texture overlay': r'grain|noise|texture',
 'chromatic dispersion / fringe': r'chromatic|fringe|dispersion|rgb-split|aberration',
 'warm off-white / cream paper instead of #fff': r'cream|paper|warm|off-white|ivory|bone',
 'tinted near-black instead of #000': r'near-black|tinted-black|ink|off-black',
 'colour derived from content/backdrop': r'from-|sampled|derived|matches|backdrop|content-colou?r',
 'state encoded redundantly (colour + shape/word)': r'shape|word|redundan|icon-plus|label-changes|tense',
 'motion: fast-start ease-out snaps': r'ease-out|snap|fast',
 'motion: staggered / sequenced reveals': r'stagger|sequenc|cascade|delay',
 'motion: blur-in / crossfade content swaps': r'blur-in|crossfade|fade|blur',
 'physical realism (shadows, depth, materials)': r'shadow|depth|material|physical|extru|emboss|deboss',
 'optical alignment / kerning / overshoot': r'optical|kern|overshoot|baseline',
 'grid-snapped / pixel-aligned construction': r'grid|pixel|snap|module',
 'consistent iconography stroke/system': r'icon|glyph|stroke-weight',
 'dot / tick / ruler indicators': r'dot|tick|ruler',
 'dashed / dotted guides & construction lines': r'dashed|dotted|guide|construction|crop',
 'copy & microcopy craft': r'copy|label|tooltip|microcopy|voice',
}
ANTI = {
 'low-contrast secondary/meta/placeholder text': r'grey|gray|secondary|meta|placeholder|hint|caption|subtitle|faint|dim|inactive|footer|tiny|small',
 'white text on light/saturated colour fills': r'white',
 'text over busy imagery / gradients / motion': r'over|busy|image|photo|gradient|video|motion-behind|behind',
 'colour-only state / semantics': r'colou?r-only|only-colou?r|red-green|hue-only|without-label|no-label',
 'hover-only / hidden affordances': r'hover|hidden|affordance|discoverab',
 'decorative motion without meaning / long loops': r'decorative|loop|gratuitous|ambient|novelty',
 'typos & copy errors': r'typo|spelling|misspel|grammar|placeholder-copy|lorem|repeated',
 'inconsistent / contradictory specs': r'inconsist|contradict|mismatch|conflict',
 'missing rules (min size, misuse, type scale, states)': r'no-|missing|without|absent|undocument',
 'unreadable rotated / warped / distorted text': r'rotated|warp|distort|refract|illegib|unreadable',
 'cropped / low-res / capture issues': r'crop|low-res|capture|blurry',
 'tiny touch targets / dense controls': r'target|dense|cramped',
}

def cluster(tag, rules):
    t = tag.lower(); return [k for k, rx in rules.items() if re.search(rx, t)]

def main():
    out = {}
    rows = []
    for p in glob.glob(os.path.join(R, 'analysis/*/*.md')):
        f = front(p)
        if f and f.get('id') and f.get('status') != 'failed': rows.append(f)
    for key, rules in (('patterns', PATTERNS), ('craft_signals', CRAFT), ('anti_patterns', ANTI)):
        hits = defaultdict(lambda: defaultdict(set)); unclustered = defaultdict(int)
        for r in rows:
            for tag in (r.get(key) or []) if isinstance(r.get(key), list) else []:
                cs = cluster(str(tag), rules)
                if not cs: unclustered[str(tag)] += 1
                for c in cs:
                    hits[c]['ALL'].add(r['id']); hits[c][f"{r['source']}:{r['category']}"].add(r['id'])
        out[key] = {c: {'n': len(g['ALL']), 'by_category': {k: len(v) for k, v in sorted(g.items()) if k != 'ALL'}, 'ids': sorted(g['ALL'])} for c, g in sorted(hits.items(), key=lambda kv: -len(kv[1]['ALL']))}
        out[key + '_unclustered_count'] = len(unclustered)
    out['n_examples'] = len(rows)
    json.dump(out, open(os.path.join(R, 'synthesis/_clusters.json'), 'w'), indent=1)
    for key in ('patterns', 'craft_signals', 'anti_patterns'):
        print('==', key, 'unclustered tags:', out[key + '_unclustered_count'])
        for c, v in out[key].items(): print(f"{v['n']:4d}  {c}")

if __name__ == '__main__':
    main()
