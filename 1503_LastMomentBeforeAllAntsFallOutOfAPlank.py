# 1st solution
# O(n) time | O(1) space
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        if left:
            ans = max(ans, max(left))
        if right:
            ans = max(ans, n - min(right))
        return ans