# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            value = num
            key = 0
            while value > 0:
                key += value % 10
                value //= 10
            if key not in dic:
                dic[key] = []
            dic[key].append(num)
            if len(dic[key]) > 2:
                dic[key].sort(reverse=True)
                dic[key].pop()
        ans = -1
        for key in dic:
            if len(dic[key]) == 2:
                ans = max(ans, sum(dic[key]))
        return ans
