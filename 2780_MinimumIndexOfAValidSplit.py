# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        val = -1
        cnt = 0
        n = len(nums)
        for num in nums:
            if num == val:
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                val = num
                cnt = 1
        k = nums.count(val)

        if k * 2 <= n:
            return -1
        
        cnt = 0
        for i in range(n - 1):
            if nums[i] == val:
                cnt += 1
            if cnt * 2 > (i + 1) and (k - cnt) * 2 > (n - i - 1):
                return i
        return -1
            
