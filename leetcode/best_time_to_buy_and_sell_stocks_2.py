class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                sum += diff
        return sum
