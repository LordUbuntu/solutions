# Jacobus Burger (2023)
# Solution:
#   Very straightforward, just read input from stdin and calculate diff.
# See:
#   https://open.kattis.com/problems/different
from sys import stdin

for line in stdin:
    a, b = map(int, line.split())
    print(abs(a - b))
