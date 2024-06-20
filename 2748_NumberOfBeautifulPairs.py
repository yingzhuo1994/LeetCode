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