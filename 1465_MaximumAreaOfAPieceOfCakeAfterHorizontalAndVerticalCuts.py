# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7

        maxSquareHeight = self.getMaxLength(horizontalCuts, h)
        maxSquareWidth = self.getMaxLength(verticalCuts, w)
        
        maxArea = maxSquareHeight * maxSquareWidth
        return maxArea % MOD

    def getMaxLength(self, cuts, L):
        maxLength = 0
        cuts.sort()
        cuts.append(L)
        lastlength = 0
        for i in range(len(cuts)):
            deltaLength = cuts[i] - lastlength
            maxLength = max(maxLength, deltaLength)
            lastlength = cuts[i]
        cuts.pop()
        return maxLength