"""Render synthesis/patterns-by-category.md from _clusters.json (counts, share, top-rated example ids)."""
import json, os, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aggregate import front
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
C = json.load(open(os.path.join(R, 'synthesis/_clusters.json')))
rows = {f['id']: f for f in (front(p) for p in glob.glob(os.path.join(R, 'analysis/*/*.md'))) if f and f.get('id') and f.get('status') != 'failed'}
tot = lambda i: sum(float(v) for v in rows[i]['scores'].values()) if isinstance(rows.get(i, {}).get('scores'), dict) else 0
cats = {}
for i, r in rows.items(): cats.setdefault(f"{r['source']}:{r['category']}", []).append(i)
L = ['# Recurring patterns by category', '',
     f"Source: {C['n_examples']} analysed examples. Tags from each analysis' front matter were mapped to canonical clusters with the transparent regex rules in `scripts/cluster_tags.py` (a tag can feed several clusters). "
     'Counts = number of distinct examples showing the pattern; ids listed are the highest-rated examples in that cluster (aesthetics+originality+usability+craft).', '']
for key, title in (('patterns', 'Components & patterns'), ('craft_signals', 'Craft signals'), ('anti_patterns', 'Anti-patterns')):
    L += [f'## {title} — all categories', '', '| # examples | cluster | best examples |', '|---:|---|---|']
    for c, v in list(C[key].items())[:40]:
        best = sorted(v['ids'], key=tot, reverse=True)[:5]
        L.append(f"| {v['n']} | {c} | {', '.join(best)} |")
    L.append('')
L += ['## Per category (components & patterns, top 10)', '']
for cat in sorted(cats, key=lambda k: -len(cats[k])):
    n = len(cats[cat]); L += [f'### {cat} — {n} examples', '', '| count | share | cluster | best examples |', '|---:|---:|---|---|']
    ranked = sorted(((v['by_category'].get(cat, 0), c, v) for c, v in C['patterns'].items()), reverse=True)[:10]
    for k, c, v in ranked:
        if not k: continue
        best = sorted([i for i in v['ids'] if i in cats[cat]], key=tot, reverse=True)[:4]
        L.append(f"| {k} | {100 * k // n}% | {c} | {', '.join(best)} |")
    L.append('')
open(os.path.join(R, 'synthesis/patterns-by-category.md'), 'w').write('\n'.join(L)); print('ok', len(L))
