"""Sample the dominant colours of images (pixel truth for the analyses).
Writes palette.json into each example dir: {file: [[hex, share%], ...]} using median-cut on a
downscaled copy, merging near-duplicates (RGB distance < 18). Also offers a WCAG contrast helper.
Usage: python3 -I palette.py [inspora|brandguidelines] [id-substring...]"""
import glob, json, os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw')

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + 0.05) / (lb + 0.05), 2)

def palette(path, n=10):
    im = Image.open(path).convert('RGB'); im.thumbnail((240, 240))
    q = im.quantize(colors=24, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette(); counts = sorted(q.getcolors(), reverse=True); total = sum(c for c, _ in counts)
    out = []
    for c, idx in counts:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        for o in out:
            if sum((a - b) ** 2 for a, b in zip(o['rgb'], rgb)) ** 0.5 < 18: o['n'] += c; break
        else: out.append({'rgb': rgb, 'n': c})
    out.sort(key=lambda o: -o['n'])
    return [['#%02x%02x%02x' % o['rgb'], round(100 * o['n'] / total, 1)] for o in out[:n]]

def targets(src, d):
    if src == 'inspora':
        return sorted(f for f in glob.glob(d + '/m*') if f.endswith(('.webp', '.png', '.jpg', '.jpeg', '.gif', '.avif')) and ('_key' in f or '_f' not in f) and '_sheet' not in f)
    return sorted(glob.glob(d + '/pages/p*.jpg') + glob.glob(d + '/tiles/*.jpg'))

if __name__ == '__main__':
    srcs = [sys.argv[1]] if len(sys.argv) > 1 else ['inspora', 'brandguidelines']
    for src in srcs:
        for d in sorted(glob.glob(os.path.join(RAW, src, '*'))):
            if not os.path.isdir(d) or os.path.basename(d).startswith('_'): continue
            if len(sys.argv) > 2 and not any(a in d for a in sys.argv[2:]): continue
            res = {}
            for f in targets(src, d):
                try: res[os.path.relpath(f, d)] = palette(f)
                except Exception as e: res[os.path.relpath(f, d)] = f'error {e}'
            if res: open(os.path.join(d, 'palette.json'), 'w').write('{\n' + ',\n'.join(f'{json.dumps(k)}: {json.dumps(v)}' for k, v in res.items()) + '\n}\n')
    print('ok')
