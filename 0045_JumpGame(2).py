# 1st solution
# O(n) time | O(1) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 1
        maxIdx = nums[0]
        curRange = nums[0]
        for i in range(1, len(nums) - 1):
            maxIdx = max(maxIdx, i + nums[i])
            curRange -= 1
            if curRange == 0:
                step += 1
                curRange = maxIdx - i
        return step

# 2nd solution, DP, TLE
# O(n^2) time | O(n) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        table = [float('inf') for _ in nums]
        table[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    table[i + j] = min(table[i + j], table[i] + 1)
        return table[-1]

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        left = right = 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
            
        return jumps