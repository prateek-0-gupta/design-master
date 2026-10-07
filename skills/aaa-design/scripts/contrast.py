#!/usr/bin/env python3
"""WCAG 2.x contrast checker + fixer.

  python3 contrast.py '#6b6b72' '#ffffff' ['#fg2' '#bg2' ...]   # check pairs
  python3 contrast.py --fix '#16a34a' '#f2f2f2' [--target 4.5]    # nearest passing fg (same hue)

Thresholds: 4.5 normal text, 3.0 large text (>=24px, or >=18.66px bold) and non-text UI (borders, icons, focus rings).
"""
import sys

def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def rgb(h):
    h = h.strip().lstrip('#')
    if len(h) == 3: h = ''.join(ch * 2 for ch in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def lum(h):
    r, g, b = (_lin(v) for v in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def mix(h, toward, t):
    a, b = rgb(h), rgb(toward)
    return '#%02x%02x%02x' % tuple(round(x + (y - x) * t) for x, y in zip(a, b))

def fix(fg, bg, target):
    """Move fg toward black or white (whichever increases contrast) until target is met."""
    toward = '#000000' if lum(bg) > 0.18 else '#ffffff'
    for i in range(0, 101):
        c = mix(fg, toward, i / 100)
        if ratio(c, bg) >= target: return c, round(ratio(c, bg), 2)
    return toward, round(ratio(toward, bg), 2)

def main(a):
    if not a or a[0] in ('-h', '--help'):
        print(__doc__); return 0
    if a[0] == '--fix':
        fg, bg = a[1], a[2]
        target = float(a[a.index('--target') + 1]) if '--target' in a else 4.5
        c, r = fix(fg, bg, target)
        print(f'{fg} on {bg}: {ratio(fg, bg):.2f}:1  ->  use {c} ({r}:1, target {target})'); return 0
    bad = 0
    for i in range(0, len(a) - 1, 2):
        r = ratio(a[i], a[i + 1])
        tag = 'AA' if r >= 4.5 else 'AA-large/UI only' if r >= 3 else 'FAIL'
        bad += r < 4.5
        print(f'{a[i]} on {a[i+1]}: {r:.2f}:1  {tag}')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
