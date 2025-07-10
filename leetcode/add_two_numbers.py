# WORK IN PROGRESS
# This really shouldn't be a hard one to do... I'll come back with fresh eyes.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode()
        sol = solution
        a = l1
        b = l2
        while (a is not None) and (b is not None):
            s = (a.val if a is not None else 0) + (b.val if b is not None else 0)
            c = s // 10
            s = s % 10

            sol.val = sol.val + s
            if (a.next is not None) and (b.next is not None):
                sol.next = ListNode(val=c)

                a = a.next
                b = b.next
                sol = sol.next
        return solution
