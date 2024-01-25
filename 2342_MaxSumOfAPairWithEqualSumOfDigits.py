# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            key = sum(map(int, str(num)))
            if key in dic:
                ans = max(ans, dic[key] + num)
                dic[key] = max(dic[key], num)
            else:
                dic[key] = num

        return ans
