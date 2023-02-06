# 1st solution
# O(n) time | O(n) space
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = [0] * (2 * n)
        for i in range(n):
            newNums[2*i] = nums[i]
            newNums[2*i+1] = nums[n + i]
        return newNums