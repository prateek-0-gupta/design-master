"""Build research/inventory.json from the raw enumeration outputs of both sources."""
import json, re, os
from collections import Counter, OrderedDict
R = os.path.join(os.path.dirname(__file__), '..')
raw = lambda *p: os.path.join(R, 'raw', *p)

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

inv = []
# ---- Inspora
posts = json.load(open(raw('inspora/_api/posts.json')))
member = json.load(open(raw('inspora/_api/membership.json')))
details_dir = raw('inspora')
for slug, p in posts.items():
    cats = sorted({m.split(':')[1] for m in member[slug] if not m.endswith(':All')})
    det_path = os.path.join(details_dir, slug, 'post.json')
    det = json.load(open(det_path)) if os.path.exists(det_path) else None
    media = det['media'] if det else p['media']
    types = Counter(m['type'] for m in media)
    inv.append(OrderedDict(
        id='insp-' + slug, source='inspora', url=f'https://www.inspora.design/posts/{slug}',
        category=(det or {}).get('category') or (cats[0] if cats else None),
        title=p['title'], creator=p['creator']['name'],
        creator_handle=(det or {}).get('creator', {}).get('handle'),
        slide_count=p.get('mediaCount', len(media)),
        asset_type='video' if set(types) == {'video'} else 'image' if set(types) == {'image'} else 'mixed' if det else p['media'][0]['type'],
        featured=any(m.startswith('featured:') for m in member[slug]),
        styles=(det or {}).get('styles'), colors=(det or {}).get('colors'), industries=(det or {}).get('industries'),
        description=(det or {}).get('description'), source_url=(det or {}).get('sourceUrl'),
        created_at=p['createdAt']))

# ---- brandguidelines.net
home = json.load(open(raw('brandguidelines/_enum/home2_cards.json')))
tmpl = json.load(open(raw('brandguidelines/_enum/templates_cards.json')))
def asset_type(u):
    if 'dropbox.com' in u or u.lower().split('?')[0].endswith('.pdf'): return 'pdf'
    if 'figma.com' in u: return 'figma-prototype'
    if re.search(r'lingoapp|corebook|brandpad|standards\.site|canva\.site|frontify', u): return 'hosted-brand-platform'
    return 'live-site'
seen = {}
section = 'hero'
order = 0
for c in home + tmpl:
    t = [x for x in c['texts'] if x != '✨ New']
    if not t or len(t) < 2: continue
    u = c['href']
    is_tmpl = '/templates/' in u or ('ui8.net' in u and '/products/' in u)
    if is_tmpl:
        price, title, vendor = t[0], t[1], t[2] if len(t) > 2 else None
        rec = OrderedDict(source='brandguidelines', url=u, category='template', title=title, creator=vendor,
                          attribution=f'Template by {vendor}', price=price, asset_type='template-page', slide_count=None)
    else:
        brand, attr = t[0], t[1]
        cat = 'promoted' if attr == 'Promoted' else 'guideline'
        rec = OrderedDict(source='brandguidelines', url=u, category=cat, title=brand,
                          creator=attr.replace('Design by ', '') if attr.startswith('Design by') else ('In-house' if attr == 'In-house' else attr),
                          attribution=attr, asset_type='promoted-site' if cat == 'promoted' else asset_type(u), slide_count=None)
    key = u.split('?')[0].rstrip('/') if 'dropbox' not in u else u.split('&')[0]
    if key in seen:
        prev = seen[key]
        if rec['attribution'] not in prev['attribution_all']: prev['attribution_all'].append(rec['attribution'])
        continue
    order += 1
    rec['id'] = 'bg-' + slugify(rec['title'])
    rec['attribution_all'] = [rec['attribution']]
    rec['list_order'] = order
    rec.move_to_end('id', last=False)
    seen[key] = rec
    inv.append(rec)
ids = Counter(r['id'] for r in inv); assert all(v == 1 for v in ids.values()), [k for k, v in ids.items() if v > 1]
json.dump(inv, open(os.path.join(R, 'inventory.json'), 'w'), indent=1, ensure_ascii=False)
c = Counter((r['source'], r['category']) for r in inv)
for k in sorted(c, key=str): print(k, c[k])
print('assets', Counter((r['source'], r['asset_type']) for r in inv))
print('total', len(inv))
