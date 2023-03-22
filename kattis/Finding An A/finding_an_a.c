// Jacobus Burger (2023)
// "Finding An 'A'"
// desc:
//      We are given a string s and want to print the substring of s
//      from si to sn where si = 'a'. In other words, print the
//      substring of s from the first 'a' to the end of s.
// solution:
//      We can get a pointer for the first 'a' in s using strchr, then
//      we just need to print that substring out.
// see: https://open.kattis.com/problems/findingana
#include <string.h>
#include <stdio.h>

int main(void) {
        char s[1000];
        scanf("%s", s);
        printf("%s\n", strchr(s, 'a'));
}
