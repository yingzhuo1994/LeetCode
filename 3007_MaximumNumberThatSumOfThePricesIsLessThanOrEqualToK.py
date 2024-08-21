# 1st solution
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def getPrice(num):
            d = x
            val = 0

            while (1 << (d - 1)) <= num:
                front = num >> d
                back = num & ((1 << (d - 1)) - 1)
                count = 0
                if num & (1 << (d - 1)):
                    count += back + 1
                count += front * (1 << (d - 1))

                val += count
                d += x

            return val

        start = 0
        end = 1 << 63
        ans = 0
        while start < end:
            mid = start + (end - start) // 2
            if getPrice(mid) <= k:
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid
        return ans
