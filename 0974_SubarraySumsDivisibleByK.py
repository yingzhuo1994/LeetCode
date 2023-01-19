# 1st solution
# O(n) time | O(min(k, n)) space
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curSum = 0
        dic = {0: 1}
        ans = 0
        for num in nums:
            curSum += num
            curSum %= k
            if curSum in dic:
                ans += dic[curSum]
            dic[curSum] = dic.get(curSum, 0) + 1
        return ans