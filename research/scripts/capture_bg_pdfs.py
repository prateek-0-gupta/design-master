"""Phase 2: download every brand-guideline PDF, render page images, extract text, build contact sheets.
Outputs in raw/brandguidelines/{id}/: doc.pdf, pages/p001.jpg (~1400 px wide), text/p001.txt,
sheets/sheet01.jpg (4x3 pages per sheet, labelled), pdf_meta.json."""
import json, os, re, subprocess, sys, glob, math
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, '..', 'raw', 'brandguidelines')
inv = [r for r in json.load(open(os.path.join(HERE, '..', 'inventory.json'))) if r['source'] == 'brandguidelines' and r['asset_type'] == 'pdf']
only = set(sys.argv[1:])

def sh(*a):
    return subprocess.run(a, check=True, capture_output=True)

def dl_url(u):
    if 'dropbox.com' in u:
        u = re.sub(r'([?&])dl=0', r'\1dl=1', u)
        if 'dl=1' not in u: u += '&dl=1'
    return u

def sheets(pages, outdir, cols=4, rows=3, tw=480):
    os.makedirs(outdir, exist_ok=True)
    per = cols * rows
    for s in range(math.ceil(len(pages) / per)):
        chunk = pages[s * per:(s + 1) * per]
        ims = [Image.open(p).convert('RGB') for p in chunk]
        th = max(int(im.height * tw / im.width) for im in ims)
        sheet = Image.new('RGB', (cols * tw + (cols + 1) * 6, rows * th + (rows + 1) * 6), (60, 60, 60))
        dr = ImageDraw.Draw(sheet)
        for k, (im, p) in enumerate(zip(ims, chunk)):
            x = 6 + (k % cols) * (tw + 6); y = 6 + (k // cols) * (th + 6)
            sheet.paste(im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS), (x, y))
            label = os.path.basename(p)[1:4]
            dr.rectangle([x, y, x + 34, y + 16], fill=(0, 0, 0)); dr.text((x + 4, y + 2), label, fill=(255, 255, 0))
        sheet.save(os.path.join(outdir, f'sheet{s + 1:02d}.jpg'), quality=85)

fails = {}
for r in inv:
    if only and r['id'] not in only: continue
    d = os.path.join(RAW, r['id']); os.makedirs(d, exist_ok=True)
    pdf = os.path.join(d, 'doc.pdf')
    try:
        if not os.path.exists(pdf):
            sh('curl', '-sSfL', '--retry', '3', '-A', 'Mozilla/5.0', '-o', pdf + '.part', dl_url(r['url']))
            with open(pdf + '.part', 'rb') as f:
                if f.read(5) != b'%PDF-': raise RuntimeError('not a PDF (got HTML/redirect)')
            os.replace(pdf + '.part', pdf)
        info = sh('pdfinfo', pdf).stdout.decode(errors='replace')
        npages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
        size = re.search(r'Page size:\s+(.*)', info).group(1)
        pdir = os.path.join(d, 'pages'); tdir = os.path.join(d, 'text'); os.makedirs(pdir, exist_ok=True); os.makedirs(tdir, exist_ok=True)
        if len(glob.glob(pdir + '/*.jpg')) < npages:
            sh('pdftoppm', '-jpeg', '-jpegopt', 'quality=85', '-scale-to-x', '1400', '-scale-to-y', '-1', pdf, os.path.join(pdir, 'p'))
            for f in glob.glob(pdir + '/p-*.jpg'):
                n = int(re.search(r'p-0*(\d+)\.jpg', f).group(1)); os.replace(f, os.path.join(pdir, f'p{n:03d}.jpg'))
        sh('pdftotext', '-layout', pdf, os.path.join(tdir, 'all.txt'))
        fonts = sh('pdffonts', pdf).stdout.decode(errors='replace')
        pages = sorted(glob.glob(pdir + '/p*.jpg'))
        sheets(pages, os.path.join(d, 'sheets'))
        json.dump(dict(pages=npages, page_size=size, bytes=os.path.getsize(pdf), fonts_raw=fonts), open(os.path.join(d, 'pdf_meta.json'), 'w'), indent=1)
        print(r['id'], npages, 'pages', size)
    except Exception as e:
        msg = getattr(e, 'stderr', b'') or b''
        fails[r['id']] = f'{e} {msg[:200]!r}'; print('FAIL', r['id'], fails[r['id']])
json.dump(fails, open(os.path.join(RAW, '_pdf_failures.json'), 'w'), indent=1)
print('failures', len(fails))
