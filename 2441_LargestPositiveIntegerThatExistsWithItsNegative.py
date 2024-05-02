# 1st solution
# O(n) time | O(n) space
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = -1
        for num in cnt:
            if num > 0 and cnt[-num] > 0:
                ans = max(ans, num)
        return ans