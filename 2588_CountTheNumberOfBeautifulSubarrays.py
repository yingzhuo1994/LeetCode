# 1st solution
# O(n) time | O(n) space
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dic = {0: 1}
        ans = 0
        prefix = 0
        for num in nums:
            prefix ^= num
            ans += dic.get(prefix, 0)
            dic[prefix] = dic.get(prefix, 0) + 1
        return ans