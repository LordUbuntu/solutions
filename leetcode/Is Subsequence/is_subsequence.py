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
