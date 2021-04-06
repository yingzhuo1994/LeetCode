class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 1st solution
        # if n == 0:
        #     return 0
        # factorial = 1
        # while n > 0:
        #     factorial *= n
        #     n -= 1
        # count = 0

        # while factorial > 0:
        #     r = factorial % 10
        #     factorial = factorial // 10
        #     if r == 0:
        #         count += 1
        #     else:
        #         break
        # return count

        # 2nd solution
        # while factorial > 9:
        #     n = len(str(factorial))
        #     mid = n // 2
        #     r = factorial % (10**mid)
        #     if r == 0:
        #         count += mid
        #         factorial = factorial // (10**mid)
        #     else:
        #         factorial = r
        # return count

        # 3rd solution
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
