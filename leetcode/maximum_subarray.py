# Maximum Subarray Problem
#   from: https://leetcode.com/problems/maximum-subarray/description/
# Kudane's Algorithm: https://www.youtube.com/watch?v=86CQq3pKSUw
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # utilizing Kudane's algorithm
        current = maximum = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maximum = max(maximum, current)
        return maximum
