# 1st solution
# O(logN) time | O(logN) space 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        divisorLst = [divisor]
        quotes = [1]
        while dividend >= divisor:
            divisor += divisor
            divisorLst.append(divisor)
            quotes.append(quotes[-1] + quotes[-1])

        ans = 0
        while dividend > 0:
            idx = bisect.bisect_right(divisorLst, dividend)
            if idx == 0:
                break
            ans += quotes[idx - 1]
            dividend -= divisorLst[idx - 1]

        if (sign1 > 0) is (sign2 > 0):
            return min(ans, 2**31-1)
        else:
            return -min(ans, 2**31)
