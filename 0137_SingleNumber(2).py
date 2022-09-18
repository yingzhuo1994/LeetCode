# 1st solution
# O(32n) time | O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        negCount = 0
        for num in nums:
            if num < 0:
                negCount += 1
        sign = 1
        if negCount % 3 != 0:
            sign = -1
        ans = 0
        for k in range(32):
            count = 0
            for num in nums:
                if (abs(num) >> k) & 1:
                    count += 1
            if count % 3 > 0:
                ans |= 1 << k
        return sign * ans

# 2nd solution
# O(32n) time | O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for k in range(32):
            count = 0
            for num in nums:
                if (num >> k) & 1:
                    count += 1
            if count % 3 != 0:
                ans |= 1 << k

        if (ans >> 31) & 1:
            return ans - (1 << 32)
        return ans