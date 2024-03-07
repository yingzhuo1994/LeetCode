# 1st solution
# O(n) time | O(n) space
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        val = 0
        ans = [0 for _ in range(len(word))]
        for i, d in enumerate(word):
            val = val * 10 + int(d)
            val %= m
            if val == 0:
                ans[i] = 1
        return ans