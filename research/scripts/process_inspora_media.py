"""Phase 2b: download every Inspora media item at full resolution.
Images are saved as-is. Videos: ffprobe metadata, 9 evenly spaced frames, a labelled 3x3 contact
sheet, one full-resolution key frame, and a motion profile (frame-difference energy over time) used
to estimate animation segment durations and easing shape. The mp4 is deleted afterwards to save disk.
Usage: python3 -I process_inspora_media.py [workers]"""
import json, os, subprocess, sys, glob, math
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from PIL import Image, ImageDraw

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'raw', 'inspora')

def sh(*a, **k):
    return subprocess.run(a, check=True, capture_output=True, **k)

def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0: return
    for attempt in range(4):
        try:
            sh('curl', '-sSfL', '--retry', '3', '-o', dest + '.part', url); os.replace(dest + '.part', dest); return
        except subprocess.CalledProcessError as e:
            err = e
    raise RuntimeError(f'download failed {url}: {err.stderr[:200]}')

def probe(path):
    out = json.loads(sh('ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                        'stream=width,height,r_frame_rate,nb_frames,codec_name:format=duration', '-of', 'json', path).stdout)
    s = out['streams'][0]; num, den = map(int, s['r_frame_rate'].split('/'))
    return dict(width=s['width'], height=s['height'], fps=round(num / den, 2), duration=float(out['format']['duration']), codec=s['codec_name'])

def motion_profile(path, meta):
    fps = min(30, meta['fps'] or 30)
    w = 128; h = max(2, int(round(meta['height'] * w / meta['width'] / 2) * 2))
    raw = sh('ffmpeg', '-v', 'error', '-i', path, '-vf', f'fps={fps},scale={w}:{h},format=gray', '-f', 'rawvideo', '-').stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
    if len(fr) < 3: return None
    d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))  # energy per frame step
    t = np.arange(1, len(fr)) / fps
    thr = max(0.35, 0.2 * float(np.percentile(d, 95)))
    moving = d > thr
    segs, i = [], 0
    while i < len(d):
        if moving[i]:
            j = i
            while j + 1 < len(d) and (moving[j + 1] or (j + 2 < len(d) and moving[j + 2]) or (j + 3 < len(d) and moving[j + 3])): j += 1
            seg = d[i:j + 1]
            dur = (j - i + 1) / fps
            if dur >= 0.1:
                pk = int(np.argmax(seg)); ratio = (pk + 0.5) / len(seg)
                cv = float(seg.std() / (seg.mean() + 1e-6))
                shape = 'continuous/linear' if (cv < 0.35 and dur > 1.0) else 'ease-out (fast start)' if ratio < 0.35 else 'ease-in (slow start)' if ratio > 0.65 else 'ease-in-out (symmetric)'
                segs.append(dict(start=round(float(t[i]) - 1 / fps, 2), end=round(float(t[j]), 2), duration=round(dur, 2), peak_at=round(ratio, 2), energy_cv=round(cv, 2), shape=shape))
            i = j + 1
        else:
            i += 1
    loop_diff = float(np.abs(fr[0] - fr[-1]).mean())
    return dict(sample_fps=fps, threshold=round(thr, 2), motion_fraction=round(float(moving.mean()), 2),
                mean_energy=round(float(d.mean()), 2), p95_energy=round(float(np.percentile(d, 95)), 2),
                first_last_diff=round(loop_diff, 2), seamless_loop_likely=bool(loop_diff < 2.0),
                segments=segs[:60], segment_count=len(segs),
                median_segment_s=round(float(np.median([s['duration'] for s in segs])), 2) if segs else None)

def contact_sheet(frames, times, out, tile_w=640):
    ims = [Image.open(f).convert('RGB') for f in frames]
    tw = tile_w; th = int(ims[0].height * tw / ims[0].width)
    cols = 3; rows = math.ceil(len(ims) / cols)
    sheet = Image.new('RGB', (cols * tw + (cols + 1) * 8, rows * th + (rows + 1) * 8), (40, 40, 40))
    dr = ImageDraw.Draw(sheet)
    for k, (im, ts) in enumerate(zip(ims, times)):
        x = 8 + (k % cols) * (tw + 8); y = 8 + (k // cols) * (th + 8)
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, y))
        dr.rectangle([x, y, x + 64, y + 18], fill=(0, 0, 0)); dr.text((x + 4, y + 3), f't={ts:.2f}s', fill=(255, 255, 0))
    sheet.save(out, quality=88)

def do_video(m, d, idx):
    mp4 = os.path.join(d, f'm{idx}.mp4'); prefix = os.path.join(d, f'm{idx}')
    if os.path.exists(prefix + '_motion.json') and os.path.exists(prefix + '_sheet.jpg'): return
    download(m['url'], mp4)
    meta = probe(mp4)
    n = 9; times = [meta['duration'] * (k + 0.5) / n for k in range(n)]
    frames = []
    for k, ts in enumerate(times):
        f = f'{prefix}_f{k}.jpg'
        sh('ffmpeg', '-v', 'error', '-y', '-ss', f'{ts:.3f}', '-i', mp4, '-frames:v', '1', '-vf', "scale='min(1600,iw)':-2", '-q:v', '3', f)
        frames.append(f)
    sh('ffmpeg', '-v', 'error', '-y', '-ss', f'{times[n // 2]:.3f}', '-i', mp4, '-frames:v', '1', '-q:v', '2', prefix + '_key.jpg')
    contact_sheet(frames, times, prefix + '_sheet.jpg')
    prof = motion_profile(mp4, meta)
    json.dump(dict(meta=meta, frame_times=[round(t, 2) for t in times], profile=prof), open(prefix + '_motion.json', 'w'), indent=1)
    os.remove(mp4)

def do_post(d):
    p = json.load(open(os.path.join(d, 'post.json')))
    for idx, m in enumerate(sorted(p['media'], key=lambda m: m.get('position', 0))):
        if m['type'] == 'image':
            ext = os.path.splitext(m['url'].split('?')[0])[1] or '.webp'
            download(m['url'], os.path.join(d, f'm{idx}{ext}'))
        else:
            do_video(m, d, idx)
    open(os.path.join(d, '_media_done'), 'w').write('ok')

def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    dirs = [os.path.dirname(f) for f in glob.glob(os.path.join(RAW, '*', 'post.json')) if not os.path.exists(os.path.join(os.path.dirname(f), '_media_done'))]
    fails = {}
    def run(d):
        try: do_post(d)
        except Exception as e: fails[os.path.basename(d)] = str(e)[:300]
    with ThreadPoolExecutor(workers) as ex: list(ex.map(run, dirs))
    prev = os.path.join(RAW, '_media_failures.json')
    json.dump(fails, open(prev, 'w'), indent=1)
    print('processed', len(dirs), 'failures', len(fails))

if __name__ == '__main__':
    main()
