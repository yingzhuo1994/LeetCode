# 1st solution
# O(n) time | O(1) space
class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for ch in n:
            ans = max(ans, int(ch))
            if ans == 9:
                break
        return ans