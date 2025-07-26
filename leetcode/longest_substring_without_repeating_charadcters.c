// Jacobus Burger (2025-07-25)
// Solution to Longest Substring Without Repeating Characters on LeetCode

int lengthOfLongestSubstring(char* s) {
    // this can be solved with a sliding window technique
    size_t l = 0, r = 0;
    int len = 0;
    while (l < strlen(s) && r < strlen(s)) {
        // scan from l to r to ensure no duplicates encountered by r
        for (int i = l; i < r; i++) {
        //  if duplicate encountered, reset l to current r
            if (s[i] == s[r]) {
                l = r;
                break;
            }
        }
        // increment len
        len = (r - l) + 1 > len ? (r - l) + 1 : len;
        // increment r
        r++;
    }
    return len;
}
