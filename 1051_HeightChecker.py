# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i, num in enumerate(heights):
            if num != expected[i]:
                ans += 1
        return ans