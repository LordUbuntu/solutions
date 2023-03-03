# I noticed that if the first character of s matches to some part of t, then we only need to see if the rest of s matches with the rest of t, for all characters in s. This seems like a DP problem then, since the optimal solution depends on solutions that follow (optimal substructure). So to solve this problem, I imagined s as sliding across t from left to right, at each point that the leftmost character of s matched to a leftmost twin in t, the problem would then subdivide into whether the remainder (substring) of has a subsequence in the remainder (substring) of t, and this question would keep going until there were no more characters.
#
# Implementing this iteratively is very simple and elegant. We go over each character of t and if we have a match with the leftmost of s, then we shorten s by removing the leftmost character and continuing across t. If we have any characters left in s, then we know s is not a subsequence of t, otherwise it is.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in t:
            if s[:1] == char:
                s = s[1:]
        if len(s) > 0:
            return False
        return True


    # alternatively, we can use two counters to compare the strings
    #   as NeetCode demonstrated in [this vid](https://www.youtube.com/watch?v=99RVfqklbCE)
    def sol2(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
