"""Sort raw captures: build raw/_by_category/{source}/{category}/{id} symlinks (no duplication) and a
committed manifest research/RAW_INDEX.md (per example: file counts by kind, sorted by source/category/id)."""
import json, os, glob
from collections import Counter
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
inv = json.load(open(os.path.join(R, 'inventory.json')))
lines = ['# Raw capture index', '', 'Raw files live in `research/raw/` (git-ignored, third-party). Sorted view: `research/raw/_by_category/{source}/{category}/{id}` (symlinks).', '']
for src in ('inspora', 'brandguidelines'):
    rows = sorted((r for r in inv if r['source'] == src), key=lambda r: (r['category'] or '', r['id']))
    lines += [f'## {src}', '', '| category | id | files | stills | video sheets | pages | tiles | notes |', '|---|---|---|---|---|---|---|---|']
    for r in rows:
        d = os.path.join(R, 'raw', src, r['id'][5:] if src == 'inspora' else r['id'])
        link = os.path.join(R, 'raw', '_by_category', src, (r['category'] or 'uncategorized').replace(' ', '_'), r['id'])
        os.makedirs(os.path.dirname(link), exist_ok=True)
        if os.path.isdir(d) and not os.path.islink(link): os.symlink(os.path.relpath(d, os.path.dirname(link)), link)
        files = [f for f in glob.glob(d + '/**/*', recursive=True) if os.path.isfile(f)]
        c = Counter()
        for f in files:
            b = os.path.basename(f)
            if '_sheet' in b: c['sheet'] += 1
            elif '/pages/' in f: c['page'] += 1
            elif '/tiles/' in f: c['tile'] += 1
            elif b.startswith('m') and b.endswith(('.webp', '.png', '.jpg', '.gif')) and '_f' not in b and '_key' not in b: c['still'] += 1
        meta = os.path.join(d, 'site_meta.json'); note = ''
        if os.path.exists(meta):
            m = json.load(open(meta)); note = 'archived (Wayback)' if m.get('archived') else ''
            if m.get('captured_from') and not m.get('archived') and m['captured_from'] != m['requested']: note = 'redirected source: ' + m['captured_from']
        lines.append(f"| {r['category']} | {r['id']} | {len(files)} | {c['still']} | {c['sheet']} | {c['page']} | {c['tile']} | {note} |")
    lines.append('')
open(os.path.join(R, 'RAW_INDEX.md'), 'w').write('\n'.join(lines))
print('ok')
