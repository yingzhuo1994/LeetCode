# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        wordSet = set()
        for word in words:
            if word[::-1] in wordSet:
                ans += 1
            wordSet.add(word)
        return ans