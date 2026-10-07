"""Slice tall full-page screenshots into viewable tiles.
Desktop shots (1440 wide) -> tiles/{name}_tNN.jpg of 1440x1800.
Mobile shots (390 CSS px, captured at DPR 2) -> downscaled to 390 wide, cut into 1500 px strips,
packed 4-up into tiles/{name}_sheetNN.jpg."""
import glob, os, sys, math
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'brandguidelines')

def tile(png):
    d = os.path.join(os.path.dirname(png), '..', 'tiles'); os.makedirs(d, exist_ok=True)
    name = os.path.splitext(os.path.basename(png))[0]
    if glob.glob(os.path.join(d, name + '_*')): return
    im = Image.open(png).convert('RGB')
    if name.startswith('m'):
        im = im.resize((390, int(im.height * 390 / im.width)), Image.LANCZOS)
        strips = [im.crop((0, y, 390, min(im.height, y + 1500))) for y in range(0, im.height, 1500)]
        for s in range(math.ceil(len(strips) / 4)):
            grp = strips[s * 4:(s + 1) * 4]
            sheet = Image.new('RGB', (4 * 390 + 5 * 10, 1500 + 20), (70, 70, 70))
            for k, st in enumerate(grp): sheet.paste(st, (10 + k * 400, 10))
            sheet.save(os.path.join(d, f'{name}_sheet{s + 1:02d}.jpg'), quality=85)
    else:
        for k, y in enumerate(range(0, im.height, 1800)):
            im.crop((0, y, im.width, min(im.height, y + 1800))).save(os.path.join(d, f'{name}_t{k + 1:02d}.jpg'), quality=85)

if __name__ == '__main__':
    for png in sorted(glob.glob(os.path.join(RAW, '*', 'shots', '*.png'))):
        if len(sys.argv) > 1 and not any(a in png for a in sys.argv[1:]): continue
        try: tile(png)
        except Exception as e: print('fail', png, e)
    print('ok')
