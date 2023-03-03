# Best Time to Sell and Buy stocks problem
#   from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# this is a classic DP, we can solve it with a sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if prices[r] < prices[l]:
                l = r
        return max_profit
