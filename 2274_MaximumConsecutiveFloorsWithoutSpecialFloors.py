# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        for i in range(len(special) - 1):
            ans = max(ans, special[i + 1] - special[i] - 1)
        ans = max(ans, special[0] - bottom, top - special[-1])
        return ans