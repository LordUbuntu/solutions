# Jacobus Burger (2023)
# Container with most water problem
# From https://leetcode.com/problems/container-with-most-water/description/
# we use a greedy approach with a shrinking window
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r])) * (r - l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
