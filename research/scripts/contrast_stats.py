"""Collect every WCAG ratio reported in the analyses -> share of examples with at least one
sub-AA text pair, distribution of minimum reported ratio. -> synthesis/_contrast_stats.json"""
import glob, json, os, re
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rows = {}
for p in glob.glob(os.path.join(R, 'analysis/*/*.md')):
    if os.path.basename(p).startswith(('AGENT', 'PROMPT')): continue
    s = open(p).read(); sec = s.split('## 4.')[1].split('## 5.')[0] if '## 4.' in s else s
    vals = [float(v) for v in re.findall(r'(\d{1,2}(?:\.\d{1,2})?)\s*:\s*1\b', sec) if 1 <= float(v) <= 21]
    if vals: rows[os.path.basename(p)[:-3]] = vals
def summary(keys):
    mins = [min(rows[k]) for k in keys]
    return dict(n=len(keys), any_below_4_5=round(100 * sum(m < 4.5 for m in mins) / len(mins), 1), any_below_3=round(100 * sum(m < 3 for m in mins) / len(mins), 1),
                median_min_ratio=sorted(mins)[len(mins) // 2], pairs_reported=sum(len(rows[k]) for k in keys),
                pairs_below_4_5_share=round(100 * sum(v < 4.5 for k in keys for v in rows[k]) / sum(len(rows[k]) for k in keys), 1))
out = {'inspora': summary([k for k in rows if k.startswith('insp-')]), 'brandguidelines': summary([k for k in rows if k.startswith('bg-')])}
json.dump(out, open(os.path.join(R, 'synthesis/_contrast_stats.json'), 'w'), indent=1); print(json.dumps(out, indent=1))
