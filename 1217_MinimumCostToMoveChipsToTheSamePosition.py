# O(n) time | O(1) space
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        for p in position:
            if p & 1:
                oddCount += 1
            else:
                evenCount += 1
        return min(oddCount, evenCount)