# 1st solution
# O(n) time | O(1) space
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            ans += all(ch in allowed for ch in word)
        return ans