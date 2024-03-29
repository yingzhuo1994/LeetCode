# 1st solution
# O(n + q) time | O(q) space
# where n is the length of nums, and q is length of queries
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in nums:
            if num % 2 == 0:
                evenSum += num
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            ans.append(evenSum)
        return ans