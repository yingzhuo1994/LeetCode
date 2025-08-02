# 1st solution
# O(n) time | O(1) space
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        if not any(ch in word for ch in "aeiouAEIOU"):
            return False
        if not any(ch.isalpha() and ch not in "aeiouAEIOU" for ch in word):
            return False
        return True