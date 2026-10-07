"""Aggregate measured motion profiles across all Inspora videos -> synthesis/_motion_stats.json"""
import glob, json, os, statistics as st
from collections import Counter
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
segs, clips, shapes, peaks = [], [], Counter(), []
for f in glob.glob(os.path.join(R, 'raw/inspora/*/m*_motion.json')):
    m = json.load(open(f)); p = m.get('profile')
    if not p: continue
    clips.append(dict(dur=m['meta']['duration'], fps=m['meta']['fps'], w=m['meta']['width'], h=m['meta']['height'], frac=p['motion_fraction'], loop=p['seamless_loop_likely'], nseg=p['segment_count']))
    for s in p['segments']:
        if s['duration'] <= 2.5:  # UI-scale transitions; longer = ambient/camera
            segs.append(s['duration']); shapes[s['shape']] += 1; peaks.append(s['peak_at'])
q = lambda a, x: round(sorted(a)[int(x * (len(a) - 1))], 2)
bins = Counter(min(int(d / 0.1) / 10, 2.0) for d in segs)
out = dict(videos=len(clips), segments=len(segs),
    duration_s=dict(p10=q(segs, .1), p25=q(segs, .25), median=q(segs, .5), p75=q(segs, .75), p90=q(segs, .9)),
    histogram_100ms={f'{k:.1f}': v for k, v in sorted(bins.items())},
    shape_share={k: round(100 * v / len(segs), 1) for k, v in shapes.most_common()},
    peak_at_median=round(st.median(peaks), 2),
    clip_duration_median=round(st.median(c['dur'] for c in clips), 2),
    fps=Counter(round(c['fps']) for c in clips).most_common(5),
    seamless_loop_share=round(100 * sum(c['loop'] for c in clips) / len(clips), 1),
    resolution_median=[st.median(c['w'] for c in clips), st.median(c['h'] for c in clips)])
json.dump(out, open(os.path.join(R, 'synthesis/_motion_stats.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
