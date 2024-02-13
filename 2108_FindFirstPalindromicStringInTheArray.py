# 1st solution
# O(kn) time | O(k) space
# where n = len(words), and k is the longest length of words
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""