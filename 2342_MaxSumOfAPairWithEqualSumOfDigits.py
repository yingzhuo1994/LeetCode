# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            value = num
            key = 0
            while value > 0:
                key += value % 10
                value //= 10
            if key in dic:
                ans = max(ans, dic[key] + num)
                dic[key] = max(dic[key], num)
            else:
                dic[key] = num

        return ans
