# 1st solution
# O(n) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        for i in range(len(nums)):
            value = abs(nums[i])
            if nums[value - 1] < 0:
                duplicate = value
                break
            else:
                nums[value - 1] *= -1
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate
    
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
    
# 3rd sorting solution
# O(nlogn) time | O(log(n)) space
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    
# 4th set solution
# O(n) time | O(n) space
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num) 

# 5th solution, Sum of Set Bits
# O(n * log(n)) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1
                    
                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1
                    
            # If the current bit is more frequently set in nums than it is in 
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask
                
        return duplicate

# 6th solution
# O(n) time | O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            key = 1 << num
            if mask & key:
                return num
            mask |= key