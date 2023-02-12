# Is Subsequence

## Problem Description
Classic Dynamic Programming problem. We want to find whether a string `s` is a subsequence of a string `t`. For example, "ace" is a subsequence of "abcde" because "a_c_e" is in "abcde", while "aec" is not a subsequence of "abcde".

## Input
Strings `s` and `t`.

## Output
`True` or `False` for whether `s` is a subsequence of `t` or not.

## Examples

### Example 1
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

### Example 2
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Solution

I noticed that if the first character of s matches to some part of t, then we only need to see if the rest of s matches with the rest of t, for all characters in s. This seems like a DP problem then, since the optimal solution depends on solutions that follow (optimal substructure). So to solve this problem, I imagined s as sliding across t from left to right, at each point that the leftmost character of s matched to a leftmost twin in t, the problem would then subdivide into whether the remainder (substring) of has a subsequence in the remainder (substring) of t, and this question would keep going until there were no more characters.

Implementing this iteratively is very simple and elegant. We go over each character of t and if we have a match with the leftmost of s, then we shorten s by removing the leftmost character and continuing across t. If we have any characters left in s, then we know s is not a subsequence of t, otherwise it is.

In pseudocode this looks like:
```
String : s, t.
foreach character in t,
  if head of s is character,
    s is s - head of s.
if s is not empty,
  return false.
otherwise,
  return true.
```
