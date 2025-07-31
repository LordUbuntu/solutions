// Jacobus Burger (2025-07-25)
// Solution to Longest Substring Without Repeating Characters on LeetCode
#include <stdio.h>
#include <string.h>


int lengthOfLongestSubstring(char* s) {
        size_t l, r, len;
        l = r = len = 0;

        // scan the string until the null terminator
        while (s[r]) {
                // across the given window
                for (int i = l; i <= r; i++) {
                        // if window is closed, count and widen
                        if (l == r) {
                                len = r - l > len ? r - l : len;
                                // r++ will be handled because of break
                                break;
                        }
                        // if any duplicates are found, count and narrow
                        for (int j = i + 1; j <= r; j++) {
                                if (s[i] == s[j]) {
                                        len = r - l > len ? r - l : len;
                                        l++;
                                        break;
                                }
                        }
                }
                // if the window passes, widen it
                r++;
        }

        // count final time if no duplicates
        bool repetition = false;
        for (int i = l; i <= r; i++)
                for (int j = i + 1; j <= r; j++)
                        if (s[i] == s[j])
                                repetition = true;
        if (!repetition)
                len = r - l > len ? r - l : len;
        else
                len = 1;

        // return solution
        return len;
}


int main(void) {
        // correct: 3 1 3 2
        char* s1 = "abcabcbb";
        char* s2 = "bbbbb";
        char* s3 = "pwwkew";
        char* s4 = "au";
        // 3 4 3 2
        // 2025-07-30 1 1 3 2
        printf("s1 %i\n", lengthOfLongestSubstring(s1));
        printf("s2 %i\n", lengthOfLongestSubstring(s2));
        printf("s3 %i\n", lengthOfLongestSubstring(s3));
        printf("s4 %i\n", lengthOfLongestSubstring(s4));
}
