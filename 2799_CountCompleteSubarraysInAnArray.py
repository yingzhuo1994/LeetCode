# 1st solution
# O(n) time | O(n) space 
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        dic = {}
        cnt = 0
        ans = 0
        start = 0
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            if dic[num] == 1:
                cnt += 1
            while cnt == distinct:
                ans += len(nums) - i
                dic[nums[start]] -= 1
                if dic[nums[start]] == 0:
                    cnt -= 1
                start += 1
        return ans