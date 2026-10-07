"""Summarize real design tokens from captured CSS + computed-style census into tokens.json per site.
Reports: custom properties grouped by kind, @font-face families, font-size values (px/rem) by frequency,
radius, box-shadow recipes, transition/animation durations and easing curves, colour literals."""
import glob, json, os, re, sys
from collections import Counter
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'brandguidelines')

def top(c, n=25): return [[k, v] for k, v in c.most_common(n)]

def summarize(d):
    css = open(os.path.join(d, 'all.css'), errors='replace').read() if os.path.exists(os.path.join(d, 'all.css')) else ''
    decl_vars = re.findall(r'(--[\w-]+)\s*:\s*([^;}{]{1,160})', css)
    groups = {'color': {}, 'font': {}, 'space': {}, 'radius': {}, 'shadow': {}, 'motion': {}, 'other': {}}
    for k, v in decl_vars:
        v = v.strip(); kl = k.lower()
        g = ('color' if re.search(r'colou?r|bg|background|fill|stroke|text-|surface|brand|primary|accent|border-c|ink|gray|grey|neutral', kl) or re.match(r'^(#|rgb|hsl|oklch|color\()', v) else
             'font' if re.search(r'font|type|text-size|leading|tracking|line-height|letter', kl) else
             'radius' if 'radius' in kl or 'rounded' in kl else
             'shadow' if 'shadow' in kl or 'elevation' in kl else
             'motion' if re.search(r'duration|ease|easing|transition|motion|timing|delay', kl) else
             'space' if re.search(r'space|spacing|gap|gutter|margin|padding|size-|sizing', kl) else 'other')
        if len(groups[g]) < 120 and k not in groups[g]: groups[g][k] = v
    ff = Counter(m.strip().strip('"\'') for m in re.findall(r'@font-face\s*{[^}]*?font-family\s*:\s*([^;]+);', css))
    fam_use = Counter(m.split(',')[0].strip().strip('"\'') for m in re.findall(r'font-family\s*:\s*([^;}]+)', css))
    sizes = Counter(re.findall(r'font-size\s*:\s*([\d.]+(?:px|rem|em|vw)|clamp\([^;}]+\))', css))
    radius = Counter(re.findall(r'border-radius\s*:\s*([^;}]+)', css))
    shadows = Counter(s.strip() for s in re.findall(r'box-shadow\s*:\s*([^;}]+)', css) if s.strip() != 'none')
    durs = Counter(re.findall(r'(?:transition|animation)[\w-]*\s*:[^;}]*?(\d*\.?\d+m?s)', css))
    eases = Counter(re.findall(r'cubic-bezier\([^)]+\)', css)) + Counter(re.findall(r'\b(ease-in-out|ease-out|ease-in|linear|steps\(\d+[^)]*\))\b', css))
    colors = Counter(c.lower() for c in re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]+\)|oklch\([^)]+\)', css))
    census = {}
    for f in sorted(glob.glob(os.path.join(d, 'census_*.json'))):
        c = json.load(open(f))
        for k in ('fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textColor', 'bg', 'radius', 'shadow', 'transition', 'border'):
            census.setdefault(k, Counter()).update(c.get(k, {}))
        census.setdefault('customProperties', {}).update(c.get('customProperties', {}))
        census.setdefault('loadedFonts', set()).update(c.get('loadedFonts', []))
    out = dict(css_bytes=len(css), custom_properties=groups, font_face_families=top(ff), font_family_usage=top(fam_use),
               css_font_sizes=top(sizes, 30), css_radius=top(radius, 15), css_shadows=top(shadows, 12),
               css_durations=top(durs, 15), css_easings=top(eases, 12), css_colors=top(colors, 30),
               rendered={k: (top(v, 25) if isinstance(v, Counter) else sorted(v) if isinstance(v, set) else dict(list(v.items())[:150])) for k, v in census.items()})
    json.dump(out, open(os.path.join(d, 'tokens.json'), 'w'), indent=1)

if __name__ == '__main__':
    for d in sorted(glob.glob(os.path.join(RAW, 'bg-*'))):
        if glob.glob(os.path.join(d, 'census_*.json')) and (len(sys.argv) < 2 or any(a in d for a in sys.argv[1:])):
            summarize(d)
    print('ok')
