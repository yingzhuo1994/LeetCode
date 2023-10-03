# 1st solution
# O(n) time | O(n) space
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                ans += dic[num]
                dic[num] += 1
        return ans