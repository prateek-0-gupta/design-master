"""WCAG 2.x contrast ratio for hex pairs. Usage: python3 -I contrast.py '#111111' '#ffffff' [...pairs]"""
import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from palette import contrast
a = sys.argv[1:]
for i in range(0, len(a) - 1, 2):
    r = contrast(a[i], a[i + 1]); print(f'{a[i]} on {a[i+1]}: {r}:1  AA-normal {"pass" if r >= 4.5 else "fail"}  AA-large {"pass" if r >= 3 else "fail"}')
