# 1st solution
# O(n) time | O(n) space
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for i, num in enumerate(nums):
            r = num - i
            dic[r] = dic.get(r, 0) + 1
        goodPairs = 0
        for value in dic.values():
            goodPairs += value * (value - 1) // 2
        return n * (n - 1) // 2 - goodPairs