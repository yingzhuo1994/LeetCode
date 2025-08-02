# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = f0 = f1 = -inf
        for x in arr:
            f1 = max(f1 + x, f0)  # 注：手动 if 比大小会更快 
            f0 = max(f0, 0) + x
            ans = max(ans, f0, f1)
        return ans