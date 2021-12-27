# 1st solution
# O(1) time | O(1) space
class Solution:
    def findComplement(self, num: int) -> int:
        result = []
        while num > 0:
            rest = num % 2
            result.append(rest)
            num >>= 1
        for i in range(len(result)):
            if result[i] == 1:
                result[i] = 0
            else:
                result[i] = 1
        ans = 0
        for i in range(len(result)):
            ans += result[i] * 2**i
        return ans

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        while n < num:
            n = (n << 1) | 1
        return n - num