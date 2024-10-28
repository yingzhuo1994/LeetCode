# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dic = {num: 1 for num in nums}
        for num in nums:
            sq = num * num
            if sq in dic:
                dic[sq] = max(dic[sq], dic[num] + 1)
        ans = max(dic.values())
        if ans == 1:
            return -1
        return ans