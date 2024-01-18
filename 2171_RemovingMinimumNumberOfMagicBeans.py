# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        ans = float("inf")
        total = sum(beans)

        n = len(beans)
        for i, bean in enumerate(beans):
            right = n - i
            curCost = total - (right * bean)
            ans = min(ans, curCost)
        
        return ans