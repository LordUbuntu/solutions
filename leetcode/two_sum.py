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
    # Originally I figured out that I could track the difference of sums against
    # the target number by finding the difference between each pair of sums and
    # the target number. This was in the right direction, but because I only
    # utilized 3 variables (a, b, c), it would get stuck on a local minimum and
    # could not find the true indices for some situations thought it worked for
    # most. Unfortunately, "mostly right" isn't good enough in computer science.
    # we need to be certain!
    def ts(self, nums, target):
        a = 0
        b = 1
        for c in range(2, len(nums)):
            # stop when we find our answer
            if nums[a] + nums[b] == target:
                return [a, b] if a < b else [b, a]
            # set a and b to pair of smallest difference to target
            ab = abs(target - (nums[a] + nums[b]))
            bc = abs(target - (nums[b] + nums[c]))
            ac = abs(target - (nums[a] + nums[c]))
            minimum = min(ab, bc, ac)
            if minimum == ab:
                a, b = a, b
            if minimum == bc:
                a, b = b, c
            if minimum == ac:
                a, b = a, c
        return [a, b] if a < b else [b, a]
    # the real solution is to take the previous improvement idea and extend it.
    # I forgot what a hashmap was but that is exactly what to use. Elements are
    # added to the hashmap after looking at them. At each element, we subtract
    # the value of the current element from the target and see if the result is
    # in the hashmap. If it is, we return the indices of both elements to
    # complete the sum.
    #
    # Once you realize you can trade linear space to get linear time, you
    # realize that you can record 'visited' numbers and thus find the solution
    # effectively.
    #
    # Lesson learned: don't overthing problems, remember basic structures, don't
    # be afraid to make tradeoffs if it's fine to do so.
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        visited = {}  # value : index
        for index, value in enumerate(nums):
            difference = target - value
            if difference in visited:
                return visited[difference], index
            visited[value] = index
