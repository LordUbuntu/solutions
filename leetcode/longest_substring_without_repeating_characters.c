// Jacobus Burger (2025-07-25)
// Solution to Longest Substring Without Repeating Characters on LeetCode
#include <stdio.h>
#include <string.h>


int lengthOfLongestSubstring(char* s) {
        // avoid all the checking work when the string is empty
        if (strlen(s) == 0)
                return 0;

        // this can be solved with a sliding window technique
        size_t l = 0, r = 1;
        int len = 0;

        // pwwke
        while (s[r] != '\0') {
                for (int i = l; i < r; i++) {
                        for (int j = l; i < r; j++) {
                                if (i == j)
                                        continue;
                                if (s[i] == s[j]) {
                                }
                        if (s[i] == s[r]) {
                                len = r - l > len ? r - l : len;
                                l++;
                                break;
                        }
                }
                r++;
        }
        return len;
}


int main(void) {
        char* s1 = "wwke";
        printf("s1 %i\n", lengthOfLongestSubstring(s1));
}
