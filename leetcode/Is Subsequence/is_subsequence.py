class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in t:
            if s[:1] == char:
                s = s[1:]
        if len(s) > 0:
            return False
        return True
