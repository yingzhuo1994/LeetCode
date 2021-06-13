class Solution:
    # 1st solution
    # O(n) time | O(1) space
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