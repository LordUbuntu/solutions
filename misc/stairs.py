# Jacobus Burger (2022-12-01)
# Thanks to NeetCode for inspiring this problem (https://www.youtube.com/watch?v=Y0lT9Fck7qI)
# Problem:
#   how many ways can we climb n stairs in 1 or 2 steps at a time?
# Solution:
#   By representing the paths up the stairs as a decision tree and counting
#   the paths that get us to the nth stair (but not beyond it) we can
#   simply implement a recursive function to search valid paths in the
#   tree. Since there are repeated subtrees, we can use caching to
#   speed up calculations through memoization.
# Example:
#   n = 3
#           0
#     1           2
#   2   3       3   X
#  3 X X X     X X 
#
# ans = 3
from functools import cache


@cache
def climb(n, step_num):
    if step_num == n:
        return 1
    if step_num > n:
        return 0
    return climb(n, step_num + 1) + climb(n, step_num + 2)




# NeetCode's Solution:
#   This solution is not mine but NeetCode's solution using DP
#   Essentially it recognizes every subtree in the decision tree
#   as a subproblem, all of which utlimately reduce to solving n and n - 1,
#   both of which remain 1, and so imagining it as a list that you solve
#   from the bottom up, we're able to find the solution by calculating the
#   previous answer as the sum of the current two knowns.
#   in other words: i_n-2 = i_n + i_n-1, going backwards to term 0.
#   Noticing a pattern, this can be calcuated without an array since it is
#   essentially the fibbonacci sequence!
def dp_climbStairs(n):
    a, b = 1, 1
    for i in range(n - 1):
        temp = a
        a = a + b
        b = temp
    return a
