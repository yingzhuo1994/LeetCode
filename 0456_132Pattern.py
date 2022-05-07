# 1st solution, TLE
# O(n^3) time | O(1) space
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    for k in range(j + 1, n):
                        if nums[i] < nums[k] < nums[j]:
                            return True
        return False

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])           
        return False