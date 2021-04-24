class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # O(logN) time | O(logN) space 
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        r = 0
        sumDivisor = 0
        divisorLst = [[1, divisor]]
        while divisor <= dividend:
            maxDivisor = divisorLst[-1][1] + divisorLst[-1][1]
            if maxDivisor <= dividend:
                curR = divisorLst[-1][0] + divisorLst[-1][0]
                divisorLst.append([curR, maxDivisor])
            for i in reversed(range(len(divisorLst))):
                if divisorLst[i][1] <= dividend:
                    dividend -= divisorLst[i][1]
                    r += divisorLst[i][0]
                    break
        if (sign1 > 0) is (sign2 > 0):
            return min(r, 2**31-1)
        else:
            return -min(r, 2**31)
