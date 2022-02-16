# 1st time
# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        lst = []
        for i in range(len(nums)):
            newNums = nums[:i] + nums[i+1:]
            curLst = [[nums[i]] + k for k in self.permute(newNums)]
            lst.extend(curLst)
        return lst

# 2nd time
# O(n*n!) time | O(n*n!) space
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationsHelper(0, nums, permutations)
        return permutations

    def permutationsHelper(self, i, nums, permutations):
        if i == len(nums) - 1:
            permutations.append(nums[:])
        else:
            for j in range(i, len(nums)):
                self.swap(nums, i, j)
                self.permutationsHelper(i + 1, nums, permutations)
                self.swap(nums, i, j)
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]