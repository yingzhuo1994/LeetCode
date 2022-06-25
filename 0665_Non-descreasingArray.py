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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        count = 0
        first = float("-inf")
        second = nums[0]

        for i in range(1, n):
            if nums[i] >= second:
                first, second = second, nums[i]
            else:
                if nums[i] >= first:
                    second = nums[i]
                count += 1
            if count > 1:
                return False
        return True

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p, n = -1, len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if p != -1:
                    return False
                p = i
        
        return p in [-1, 0, n-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]