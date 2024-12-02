# 1st solution
# O(n) time | O(n) space
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = sentence.split()
        for i, word in enumerate(lst, 1):
            if word.startswith(searchWord):
                return i
        return -1