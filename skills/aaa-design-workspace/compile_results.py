"""Unblind grading.json files and print a per-eval table (raw + capped totals, gates) for an iteration."""
import json, os, sys
IT = sys.argv[1]
obj = json.load(open(os.path.join(IT, 'objective.json'))) if os.path.exists(os.path.join(IT, 'objective.json')) else {}
names = {e['id']: e['name'] for e in json.load(open('/home/user/design-master/skills/aaa-design/evals/evals.json'))['evals']}
rows = []
for ev in sorted(d for d in os.listdir(IT) if d.startswith('eval-')):
    key = json.load(open(os.path.join(IT, ev, 'blind_key.json'))); g = json.load(open(os.path.join(IT, ev, 'blind', 'grading.json')))
    out = {}
    for lab, cfg in key.items():
        s = g[lab]; out[cfg] = dict(raw=s.get('raw_total', s.get('total')), capped=s.get('capped_total'), axes=s.get('axes'),
                                   gates=f"{obj.get(ev, {}).get(cfg, {}).get('gates_passed')}/{obj.get(ev, {}).get(cfg, {}).get('gates_total')}")
    out['winner'] = key[g['winner']]; out['why'] = g.get('why', '')
    rows.append((ev, out))
print('| Eval | With skill raw / capped | Gates | Without skill raw / capped | Gates | Blind winner |')
print('|---|---|---|---|---|---|')
for ev, o in rows:
    w, b = o['with_skill'], o['without_skill']
    print(f"| {ev} {names[int(ev.split('-')[1])]} | {w['raw']} / {w['capped']} | {w['gates']} | {b['raw']} / {b['capped']} | {b['gates']} | {o['winner']} |")
json.dump(rows, open(os.path.join(IT, 'results.json'), 'w'), indent=1)
