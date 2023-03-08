# Jacobus Burger (2023)
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





# TODO: better solution
