class Solution:
    # This can be done in O(n**2) by just checking every combo of numbers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(len(nums)):
                if a == b:
                    continue
                if nums[a] + nums[b] == target:
                    return sorted([a, b])
    # But there is a better way...
