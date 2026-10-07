"""Token benchmarks from real computed styles of captured brand/product sites (census_*.json).
Per site: body size (most frequent text size), display size (largest), step ratios of the used scale,
body line-height ratio, display tracking (em), radii, transition durations. -> synthesis/_token_bench.json"""
import glob, json, os, re, statistics as st
from collections import Counter
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
px = lambda s: float(re.match(r'[\d.]+', s).group()) if re.match(r'[\d.]+', s or '') else None
sites = {}
for d in sorted(glob.glob(os.path.join(R, 'raw/brandguidelines/bg-*'))):
    cs = [json.load(open(f)) for f in glob.glob(d + '/census_*.json')]
    if not cs: continue
    meta = json.load(open(d + '/site_meta.json'))
    if re.search(r'figma\.com|just a moment|not found|404', (meta.get('final', '') + meta.get('title', '')).lower()): continue
    sizes, pairs, radii, trans = Counter(), Counter(), Counter(), Counter()
    for c in cs:
        for k, v in c.get('fontSize', {}).items(): sizes[round(px(k))] += v
        for k, v in c.get('typePairs', {}).items(): pairs[k] += v
        for k, v in c.get('radius', {}).items():
            for p in k.split():
                x = px(p)
                if x is not None and '%' not in p: radii[min(int(x), 9999)] += v
        for k, v in c.get('transition', {}).items():
            for m in re.findall(r'([\d.]+)s', k): trans[float(m)] += v
    if not sizes: continue
    body = max((s for s in sizes if 12 <= s <= 22), key=lambda s: sizes[s], default=16)
    used = sorted(s for s, n in sizes.items() if n >= 2 and s >= 10)
    display = max(used) if used else body
    steps = [round(b / a, 3) for a, b in zip(used, used[1:]) if b / a > 1.04]
    lh = []; trk = []
    for k, v in pairs.items():
        fam, size, wt, lhs, ls = [x.strip() for x in k.split('|')]
        s = px(size); l = px(lhs.replace('lh ', '')); t = ls.replace('ls ', '')
        if s and l and abs(s - body) < 0.6: lh += [l / s] * v
        if s and s >= 32 and t != 'normal' and px(t.lstrip('-')) is not None: trk += [(-1 if t.startswith('-') else 1) * px(t.lstrip('-')) / s] * v
    sites[os.path.basename(d)] = dict(body_px=body, display_px=display, scale_steps=len(used), median_step_ratio=round(st.median(steps), 3) if steps else None,
        display_over_body=round(display / body, 2), body_line_height=round(st.median(lh), 2) if lh else None,
        display_tracking_em=round(st.median(trk), 3) if trk else None, top_radii=[r for r, _ in radii.most_common(4)],
        transitions_s=[t for t, _ in trans.most_common(4)])
def dist(key):
    v = [s[key] for s in sites.values() if s.get(key) is not None]
    return dict(n=len(v), p25=sorted(v)[len(v) // 4], median=st.median(v), p75=sorted(v)[3 * len(v) // 4], min=min(v), max=max(v)) if v else None
summary = {k: dist(k) for k in ('body_px', 'display_px', 'scale_steps', 'median_step_ratio', 'display_over_body', 'body_line_height', 'display_tracking_em')}
summary['radius_frequency'] = Counter(r for s in sites.values() for r in s['top_radii']).most_common(15)
summary['transition_frequency_s'] = Counter(t for s in sites.values() for t in s['transitions_s']).most_common(12)
json.dump(dict(summary=summary, sites=sites), open(os.path.join(R, 'synthesis/_token_bench.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))
