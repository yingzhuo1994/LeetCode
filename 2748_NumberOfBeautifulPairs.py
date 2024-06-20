# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = int(str(nums[i])[0])
                b = int(str(nums[j])[-1])
                if gcd(a, b) == 1:
                    ans += 1
        return ans

# 2nd solution
# O(n * (k + logU)) time | O(k) time
# where n = len(nums), k = 10, U = max(nums)
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = [0] * 10
        for x in nums:
            for y, c in enumerate(cnt):
                if c and gcd(y, x % 10) == 1:
                    ans += c
            while x >= 10: 
                x //= 10
            cnt[x] += 1  # 统计最高位的出现次数
        return ans