"""Phase 4 helper: parse the YAML-ish front matter of every analysis and emit frequency tables
(styles, patterns, craft signals, anti-patterns, type classes, radii, motion durations, scores)
per source/category with the example ids behind each item -> research/synthesis/_aggregate.json + .md"""
import glob, json, os, re, statistics as st
from collections import defaultdict, Counter
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def parse_val(v):
    v = v.strip()
    if v in ('null', '~', ''): return None
    if v.startswith('[') or v.startswith('{'):
        j = re.sub(r'([{,]\s*)([A-Za-z_][\w-]*)\s*:', r'\1"\2":', v)          # quote keys
        j = re.sub(r'(?<=[\[,:])\s*([A-Za-z#][^,\[\]{}"]*?)\s*(?=[,\]}])', lambda m: json.dumps(m.group(1)) if m.group(1) not in ('true', 'false', 'null') else m.group(1), j)
        try: return json.loads(j)
        except Exception: return v
    return v.strip('"')

def front(path):
    s = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', s, re.S)
    if not m: return None
    d = {}
    for line in m.group(1).splitlines():
        line = re.sub(r'\s+#.*$', '', line)
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1); d[k.strip()] = parse_val(v)
    d['_words'] = len(s.split())
    return d

def main():
    rows = [f for f in (front(p) for p in sorted(glob.glob(os.path.join(R, 'analysis', '*', '*.md')))) if f and f.get('id')]
    agg = {'n': len(rows), 'by_group': {}}
    groups = defaultdict(list)
    for r in rows:
        groups[f"{r.get('source')}:{r.get('category')}"].append(r); groups[f"{r.get('source')}:ALL"].append(r); groups['ALL'].append(r)
    for g, rs in sorted(groups.items()):
        out = {'n': len(rs), 'failed': [r['id'] for r in rs if r.get('status') == 'failed']}
        ok = [r for r in rs if r.get('status') != 'failed']
        for key in ('styles', 'patterns', 'craft_signals', 'anti_patterns', 'type_class', 'mode'):
            c = defaultdict(list)
            for r in ok:
                vals = r.get(key) or []
                for v in (vals if isinstance(vals, list) else [vals]): c[str(v)].append(r['id'])
            out[key] = sorted(([k, len(v), v] for k, v in c.items()), key=lambda x: -x[1])
        sc = defaultdict(list)
        for r in ok:
            s = r.get('scores')
            if isinstance(s, dict):
                for k, v in s.items():
                    try: sc[k].append(float(v))
                    except Exception: pass
        out['scores'] = {k: dict(mean=round(st.mean(v), 2), median=st.median(v), n=len(v)) for k, v in sc.items() if v}
        radii = Counter(); durs = []
        for r in ok:
            for x in (r.get('radius_px') or []) if isinstance(r.get('radius_px'), list) else []:
                radii[str(x)] += 1
            mo = r.get('motion')
            if isinstance(mo, dict) and isinstance(mo.get('durations_s'), list):
                durs += [float(x) for x in mo['durations_s'] if re.match(r'^[\d.]+$', str(x))]
        out['radius_px'] = radii.most_common(20)
        if durs: out['motion_durations'] = dict(n=len(durs), median=round(st.median(durs), 2), p25=round(sorted(durs)[len(durs) // 4], 2), p75=round(sorted(durs)[3 * len(durs) // 4], 2))
        ranked = sorted(ok, key=lambda r: -sum(float(v) for v in (r.get('scores') or {}).values() if re.match(r'^[\d.]+$', str(v))) if isinstance(r.get('scores'), dict) else 0)
        out['top10'] = [[r['id'], r.get('scores')] for r in ranked[:10]]
        out['bottom10'] = [[r['id'], r.get('scores')] for r in ranked[-10:]]
        agg['by_group'][g] = out
    os.makedirs(os.path.join(R, 'synthesis'), exist_ok=True)
    json.dump(agg, open(os.path.join(R, 'synthesis', '_aggregate.json'), 'w'), indent=1)
    print('analyses parsed', len(rows))
    for g, o in agg['by_group'].items(): print(g, o['n'], 'failed', len(o['failed']), o.get('scores', {}).get('craft'))

if __name__ == '__main__':
    main()
