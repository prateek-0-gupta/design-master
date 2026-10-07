"""Group ready-but-unassigned Inspora posts (media done, no analysis yet) into batches by category."""
import json, os, glob, sys
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
size = int(sys.argv[1]) if len(sys.argv) > 1 else 12
inv = [r for r in json.load(open(os.path.join(R, 'inventory.json'))) if r['source'] == 'inspora']
bd = os.path.join(R, 'analysis', '_batches'); os.makedirs(bd, exist_ok=True)
assigned = set()
for f in glob.glob(bd + '/*.txt'): assigned |= set(open(f).read().split())
ready = [r for r in inv if os.path.exists(os.path.join(R, 'raw/inspora', r['id'][5:], '_media_done'))
         and r['id'] not in assigned and not os.path.exists(os.path.join(R, 'analysis/inspora', r['id'] + '.md'))]
ready.sort(key=lambda r: (r['category'] or '', r['id']))
n0 = len(glob.glob(bd + '/insp_*.txt'))
for i in range(0, len(ready), size):
    name = os.path.join(bd, f'insp_{n0 + i // size + 1:02d}.txt')
    open(name, 'w').write(' '.join(r['id'] for r in ready[i:i + size]) + '\n'); print(name, len(ready[i:i + size]))
