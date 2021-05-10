class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        last = self.subsets(nums[1:])
        lst = [[nums[0]] + elem for elem in last] + last
        return lst
