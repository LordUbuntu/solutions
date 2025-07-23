// Jacobus Burger (2025) solution
#include <stdio.h>
#include <stdlib.h>


// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
        struct ListNode* solution = (struct ListNode*) malloc(sizeof(struct ListNode));
        solution->val = 0;
        solution->next = NULL;
        struct ListNode* current = solution;
        int carry = 0;
        printf("(0) %i %i, (h) %i %i, c %i\n", solution->val, solution->next, current->val, current->next, carry);

        while (l1 != NULL && l2 != NULL && carry != 0) {
                printf("  l1 %i %i, l2 %i %i, c %i\n", l1->val, l1->next, l2->val, l2->next, carry);
                int sum = l1->val + l2->val + carry;
                carry = sum / 10;
                struct ListNode* next = (struct ListNode*) malloc(sizeof(struct ListNode));
                next->val = sum % 10;
                next->next = NULL;
                current->next = next;
                current = current->next;
        }
        return result;
}
