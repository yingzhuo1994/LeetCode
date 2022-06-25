# 1st solution
# O(n) time | O(n) space
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        count = 0
        stack = [float("-inf"), nums[0]]

        for i in range(1, n):
            if nums[i] >= stack[-1]:
                stack.append(nums[i])
            else:
                if nums[i] >= stack[-2]:
                    stack[-1] = nums[i]
                count += 1
            if count > 1:
                return False
        return True
