# Jacobus Burger (2023)
# Find the Index of the First Occurence in a String
# See: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # pass pointer h across the haystack until it matches the first character of needle
        # when it matches, pass the pointer n from h for the length of needle
        #   if there is any mismatch, skip n chars
        #   if there is no mismatch, return the index (pointer h)
        # if needle is bigger than haystack, or h passes entire haystack, return -1
        for h in range(len(haystack)):
            if needle[0] == haystack[h]:
                for n in range(len(needle)):
                    if h + n > len(haystack) - 1:
                        return -1
                    if needle[n] != haystack[h + n]:
                        h += n
                        break
                else:
                    return h
        return -1
