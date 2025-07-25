# Jacobus Burger (2025-07-10)
# Solution to Add Two Numbers on LeetCode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution
# Stats:
# - 5ms runtime, beats 42.55%
# - 17.80MB memory, beats 84.93%
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode()
        head = solution
        carry = 0
        while l1 or l2 or carry != 0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10

            head.next = ListNode(val=sum % 10)
            head = head.next
            l1 = (l1.next if l1 is not None else None)
            l2 = (l2.next if l2 is not None else None)
        return solution.next
