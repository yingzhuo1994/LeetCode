# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda v: -v[1])
        totalUnits = 0
        for boxNum, boxValue in boxTypes:
            n = min(boxNum, truckSize)
            totalUnits += n * boxValue
            truckSize -= n
            if truckSize == 0:
                break
        return totalUnits