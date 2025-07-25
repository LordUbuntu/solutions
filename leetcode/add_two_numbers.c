// Jacobus Burger (2025-07-24)
// Solution to Add Two Numbers on LeetCode
#include <stdio.h>
#include <stdlib.h>


// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};


// Solution
// Stats:
// - 0ms runtime, beats 100%
// - 12.74MB memory, beats 36.68%
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode solution = {0, NULL};
    struct ListNode* current = &solution;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int a = l1 != NULL ? l1->val : 0;
        int b = l2 != NULL ? l2->val : 0;
        int sum = a + b + carry;
        carry = sum / 10;

        struct ListNode* next = (struct ListNode*) malloc(sizeof(struct ListNode));
        next->val = sum % 10;
        next->next = NULL;

        current->next = next;
        current = current->next;
        l1 = l1 != NULL ? l1->next : NULL;
        l2 = l2 != NULL ? l2->next : NULL;
    }
    return solution.next;
}
