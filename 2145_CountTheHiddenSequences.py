# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        val = 0
        minVal = 0
        maxVal = 0
        for diff in differences:
            val += diff
            minVal = min(minVal, val)
            maxVal = max(maxVal, val)
        bound = maxVal - minVal
        ans = upper - lower - bound + 1
        ans = max(ans, 0)
        return ans