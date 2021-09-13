class Solution:
    # 1st solution
    # O(n^(m/c + 1)) time | O(m/c) space
    # where n = len(candidateds), m = target, c = min(candidates)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)

    # 2nd solution
    # O(n^(m/c + 1)) time | O(m/c) space
    # where n = len(candidateds), m = target, c = min(candidates)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, 0, target, [], ret)
        return ret
    
    def dfs(self, nums, start, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(start, len(nums)):
            self.dfs(nums, i, target - nums[i], path + [nums[i]], ret)