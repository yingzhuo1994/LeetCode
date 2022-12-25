# 1st solution
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            nums[i + 1] += nums[i]

        ans = []
        for query in queries:
            idx = bisect.bisect_right(nums, query)
            ans.append(idx) 
        return ans