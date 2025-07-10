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
        head = solution
        carry = 0

        while (l1 is not None) and (l2 is not None) and carry == 0:
            # calculate sum and carry of current digits
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            carry = sum // 10

            # store values in current and next node
            head.next = ListNode(val=sum % 10)

            # progress to next digits
            l1 = l1.next
            l2 = l2.next
            head = head.next

        return solution.next
