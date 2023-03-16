# 1st solution
# O(n) time | O(n) space
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return str(nums[0]) + "/" + "(" + "/".join([str(nums[i]) for i in range(1, n)]) + ")"