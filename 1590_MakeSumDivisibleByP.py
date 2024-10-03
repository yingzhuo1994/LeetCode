# 1st solution
# O(n) time | O(p) space
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        dic = {}
        curSum = 0
        n = len(nums)
        ans = n
        for i in reversed(range(n)):
            r = (total - curSum) % p
            dic[r] = i
            num = nums[i]
            
            curSum += num
            val = total + (total - curSum)
            r1 = val % p
            if r1 in dic:
                ans = min(ans, dic[r1] - i + 1)

        return -1 if ans == n else ans