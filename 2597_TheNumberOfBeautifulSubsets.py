# 1st solution
# O(2^n) time | O(n) space
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        def dfs(idx, lst):
            if idx == len(nums):
                return len(lst) > 0
            count = 0
            count += dfs(idx + 1, lst)
            i = bisect.bisect_left(lst, nums[idx] - k)
            if i < len(lst) and lst[i] == nums[idx] - k:
                return count
            count += dfs(idx + 1, lst + [nums[idx]])
            return count
        return dfs(0, [])