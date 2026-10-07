"""Audit every eval output uniformly and prepare blind A/B packets for graders.
Usage: python3 run_eval_audits.py <iteration_dir>"""
import json, os, random, subprocess, sys, shutil
IT = os.path.abspath(sys.argv[1]); AUDIT = '/home/user/design-master/skills/aaa-design/scripts/audit.mjs'
random.seed(42 + len(IT))
summary = {}
for ev in sorted(os.listdir(IT)):
    if not ev.startswith('eval-'): continue
    res = {}
    for cfg in ('with_skill', 'without_skill'):
        html = os.path.join(IT, ev, cfg, 'outputs', 'index.html')
        out = os.path.join(IT, ev, cfg, 'audit_final')
        if not os.path.exists(html): res[cfg] = {'missing': True}; continue
        subprocess.run(['node', AUDIT, html, out], capture_output=True, timeout=240)
        r = json.load(open(os.path.join(out, 'report.json')))
        res[cfg] = dict(hard_fails=r['hardFails'], gates_passed=sum(v.get('pass') is not False for v in r['gates'].values()), gates_total=len(r['gates']),
                        contrast_fails=len(r['contrastFails']), worst_ratio=min([f['ratio'] for f in r['contrastFails']] or [21]),
                        overflow390=r['widths']['390']['overflowPx'], small_targets=len(r['widths']['390']['smallTargets']),
                        fonts=len(r['fontFamilies']), radii=len(r['radii']), warnings=r['warnings'], reduced_motion_css=r['reducedMotionCSS'])
    # blind packet
    order = ['with_skill', 'without_skill']; random.shuffle(order)
    pk = os.path.join(IT, ev, 'blind'); os.makedirs(pk, exist_ok=True)
    for label, cfg in zip('AB', order):
        d = os.path.join(pk, label); os.makedirs(d, exist_ok=True)
        src = os.path.join(IT, ev, cfg, 'audit_final')
        if os.path.exists(src):
            for f in ('shot-1440.png', 'shot-390.png', 'report.md'): shutil.copy(os.path.join(src, f), os.path.join(d, f))
        import re
        h = open(os.path.join(IT, ev, cfg, 'outputs', 'index.html'), encoding='utf-8').read()
        h = re.sub(r'<!--.*?-->', '', h, flags=re.S); h = re.sub(r'/\*.*?\*/', '', h, flags=re.S)
        h = re.sub(r'(?i)aaa-design|skill|rubric|audit', 'x', h)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
        # scrub the audit path from report.md so the config name doesn't leak
        p = os.path.join(d, 'report.md'); t = open(p).read().replace(cfg, label); open(p, 'w').write(t)
    json.dump({'A': order[0], 'B': order[1]}, open(os.path.join(IT, ev, 'blind_key.json'), 'w'))
    summary[ev] = res
json.dump(summary, open(os.path.join(IT, 'objective.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))
