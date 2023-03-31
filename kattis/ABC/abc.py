# Jacobus Burger (2023)
# Solution:
#   Very simple. We take the input and find their order based on the
#   relation `A <= B <= C`, then we give back the number for each letter
#   in their desired order.
# See:
#   https://open.kattis.com/problems/abc
A, B, C = sorted(map(int, input().split()))
print(' '.join([str(eval(letter)) for letter in input()]))
