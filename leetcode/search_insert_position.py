# Jacobus Burger (2023)
# O(log n) worst-case solution, using binary search
# see:
#   https://leetcode.com/problems/search-insert-position/description/
#   https://en.wikipedia.org/wiki/Binary_search_algorithm
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # because nums is sorted, we can use a classic binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]
            if target == value:
                return mid
            elif target >= value:
                left = mid + 1
            elif target < value:
                right = mid - 1
        # left will always end on the last index it might have been at, which is where it would be if inserted in order
        return left
