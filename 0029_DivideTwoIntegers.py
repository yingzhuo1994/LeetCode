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

# 2nd solution
# O(1) time | O(1) space 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for x in reversed(range(32)):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res