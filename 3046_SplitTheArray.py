# 1st solution
# O(n) time | O(n) space
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
            if cnt[num] > 2:
                return False
        return True