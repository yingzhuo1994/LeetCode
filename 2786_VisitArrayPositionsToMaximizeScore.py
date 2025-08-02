# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        if nums[0] & 1:
            maxOdd = nums[0]
            maxEven = nums[0] - x
        else:
            maxOdd = nums[0] - x
            maxEven = nums[0]
        
        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            if num & 1:
                val = max(maxOdd, maxEven - x) + num
                maxOdd = max(maxOdd, val)
            else:
                val = max(maxOdd - x, maxEven) + num
                maxEven = max(maxEven, val)

        return max(maxEven, maxOdd)
        