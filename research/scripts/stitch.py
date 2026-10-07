"""Stitch viewport screenshots of an inner scroller. Args: out.png top clientHeight part_*_{scrollTop}.png...
First part kept whole (includes fixed header); later parts contribute the scroller band, offset by actual scrollTop."""
import sys, re
from PIL import Image
out, top, ch, parts = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:]
ims = [Image.open(p).convert('RGB') for p in parts]
sts = [int(re.search(r'_(\d+)\.png$', p).group(1)) for p in parts]
W, H = ims[0].size
total = top + sts[-1] + ch + max(0, H - top - ch)
canvas = Image.new('RGB', (W, total), (255, 255, 255))
canvas.paste(ims[0], (0, 0))
for im, st in zip(ims[1:], sts[1:]):
    band = im.crop((0, top, W, min(H, top + ch)))
    canvas.paste(band, (0, top + st))
canvas.save(out)
