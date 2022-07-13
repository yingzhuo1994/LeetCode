# 1st solution
# O(n^3) time | O(1) space
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False
    
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = nums[:]
        right = nums[:]
        
        n = len(nums)
        for i in range(1, n):
            left[i] = min(left[i-1], left[i])
        
        for i in reversed(range(n-1)):
            right[i] = max(right[i+1], right[i])
        
        for i in range(n):
            if left[i] < nums[i] < right[i]:
                return True
        
        return False