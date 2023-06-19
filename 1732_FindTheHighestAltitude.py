# 1st solution
# O(n) time | O(1) space
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        cur = 0
        for alt in gain:
            cur += alt
            ans = max(ans, cur)
        return ans