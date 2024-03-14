# 1st solution
# O(n) time | O(n) space
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0: 1}
        curSum = 0
        ans = 0
        for num in nums:
            curSum += num
            target = curSum - goal
            if target in dic:
                ans += dic[target]
            dic[curSum] = dic.get(curSum, 0) + 1
        return ans
