// Jacobus Burger (2025-07-25)
// Solution to Longest Substring Without Repeating Characters on LeetCode
#include <stdio.h>
#include <string.h>


// alternative approach: record occurences of ascii characters (their
//      ascii value being their index in the array) and when it is
//      encountered again, then skip. Still using a sliding window,
//      though that too can be passed on by using a counter that gets
//      reset by repetitions, i'll need to investigate that idea...
// another inspiration could be to use something like a monotonic
//      queue, a "set" kind of, which will count its length and reset
//      when a duplicate is encountered.
int length_hash(char* s) {
        int i = 0;
        char occurence[128];
}


// an improvement might be to flip logic and only count it when an iteration passes checks?
// first successful solution, 2025-07-31
int lengthOfLongestSubstring(char* s) {
        size_t l, r, len;
        l = r = len = 0;

        // scan the string
        while (s[r]) {
                // across the given window
                for (int i = l; i <= r; i++) {
                        // if window is closed, count and widen
                        if (l == r) {
                                len = r - l > len ? r - l : len;
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
                // widen window
                r++;
        }

        // update length at end if no repetitions found
        bool rep = false;
        for (int i = l; i <= r; i++)
                for (int j = i + 1; j <= r; j++)
                        if (s[i] == s[j])
                                rep = true;
        if (!rep)
                len = r - l > len ? r - l : len;

        // return solution
        return len;
}


int main(void) {
        // correct: 3 1 3 2
        char* s1 = "abcabcbb";
        char* s2 = "bbbbb";
        char* s3 = "pwwkew";
        char* s4 = "au";
        printf("s1 %i\n", lengthOfLongestSubstring(s1));
        printf("s2 %i\n", lengthOfLongestSubstring(s2));
        printf("s3 %i\n", lengthOfLongestSubstring(s3));
        printf("s4 %i\n", lengthOfLongestSubstring(s4));
}
