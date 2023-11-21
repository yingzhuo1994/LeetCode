# 1st solution
# O(n) time | O(n) space
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            ans = 0
            while num > 0:
                ans = ans * 10 + (num % 10)
                num //= 10
            return ans
        dic = {}
        for num in nums:
            diff = num - rev(num)
            dic[diff] = dic.get(diff, 0) + 1
        MOD = 10**9 + 7
        ans = 0
        for k in dic.values():
            ans += (k - 1) * k // 2
            ans %= MOD
        return ans