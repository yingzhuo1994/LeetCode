# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]

        return sum([abs(num - median) for num in nums])

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))

# 3rd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        left, right = 0, len(nums) - 1
        while left < right:
            moves += nums[right] - nums[left]
            left += 1
            right -= 1
        return moves