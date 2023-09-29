# 1st solution
# O(n) time | P(1) space
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True

        if nums[1] - nums[0] > 0:
            status = 1
        elif nums[1] - nums[0] < 0:
            status = -1
        else:
            status = 0
        
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if status > 0:
                if diff < 0:
                    return False
            elif status < 0:
                if diff > 0:
                    return False
            else:
                status = diff
        
        return True