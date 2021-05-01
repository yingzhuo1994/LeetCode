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
