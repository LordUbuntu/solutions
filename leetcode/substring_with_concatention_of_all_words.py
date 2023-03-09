# Jacobus Burger (2023)
# see: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
# My first solution to a hard string problem. This is the most straight-forward approach, and it passes the time limit, but it has a terrible time complexity of roughly O(n**2).
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # preconditions to end early on
        if any(word not in s for word in words):  # there is a word we can't match somewhere in s
            return []
        
        # DP solution, iteratively match word slices (substrings)
        #   against the collection of yet unmatched words, if they
        #   all match (no unmatched words left) then we've found
        #   a substring with concatenation of all words, if any
        #   slice doesn't match the remaining words, then we've reached
        #   an invalid substring and can quit, moving to the next one.
        # To accomplish this, we use a left and right pointer in an
        #   outer and innter loop, the left pointer represents the left
        #   end of our sliding window, the right pointer represents the
        #   current substring partition we're matching against our
        #   list of unmatched words. We move r with l when we move l, but
        #   for every l we move r on its own to check substrings ahead.
        # The time complexity is laughably bad. This should be 
        # approximately O(n * n/m) where m is words[i].length
        indices = []  # the starts of each substring w/ concat all words
        word_length = len(words[0])  # len of word (size of substrs)
        unmatched = words.copy()  # the list of words yet unmatched
        l = r = 0  # left and right pointers of window
        while l < len(s):
            while r < len(s):
                word = s[r : r + word_length]
                if word in unmatched:
                    unmatched.remove(word)
                else:
                    break
                if unmatched == []:
                    indices.append(l)
                    break
                r += word_length
            l += 1
            r = l
            unmatched = words.copy()
        return indices





# This is my better solution using dictionaries and other optimizations.
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # This time around is better, I use two counters (dictionaries of occurences) to keep a memo
        #   of how many times each word has occured in the current substring we're scanning (the inner loop,
        #   the window from left pointer to right pointer) and then I scan across that growing window until
        #   I encounter either a word that is not in words, or more words than there is a count of, and quit
        #   early, unless the occurences of substrings in match is the same as in count, then the left index
        #   is recorded and we continue.
        # One optimization that can be carried to the previous solution is realizing that we can quit early once
        #   the left pointer has reached the last spot it can that would still allow the length of a full
        #   concatenated substring of words to fit into the "frame" of the string s, and that we only need to
        #   iterate the right pointer for the length of the full concatenated substirng of words as well, which
        #   reduces the amount of work that needs to be done.
        # Another improvement here that can be carried elsewhere is the utilization of a memo with a hashtable (a dictionary)
        #   instead of relying on constant copying and removing from lists (which add to time complexity).
        word_length = len(words[0])   # length of each word
        combo_length = len(words) * word_length  # length of any concat substr
        count = Counter(words)  # memo of occurences of each word in words
        indices = []  # start of complete concat substr
        for left in range(len(s) - combo_length + 1):
            match = Counter()
            for right in range(left, left + combo_length, word_length):
                word = s[right : right + word_length]
                if word not in count:
                    break
                match[word] += 1
                if match[word] > count[word]:
                    break
                if match == count:
                    indices.append(left)
                    break
        return indices
