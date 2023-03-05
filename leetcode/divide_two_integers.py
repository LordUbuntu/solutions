# see: https://leetcode.com/problems/divide-two-integers/description/
# standard euclidean division is not fast enough for what is being done, and I refuse to write a lookup table to do SRT division, here is the compounding euclidean solution O(log n) instead of O(n). Credit to Timothy H Chang for showing this trick, I need more practice. There's a binary long division approach I know that I might add later. It's a hassle to make though, and it might not be the fastest either.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = abs(dividend)
        d = abs(divisor)
        count = 0
        while n >= d:
            tmp = d
            mul = 1
            while n >= tmp:
                count += mul
                n -= tmp
                mul += mul
                tmp += tmp
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            count = -count
        return min(2147483647, max(-2147483648, count))
