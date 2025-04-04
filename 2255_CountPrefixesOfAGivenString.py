# 1st solution
# O(n) time | O(1) space
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            if s.startswith(word):
                ans += 1
        return ans