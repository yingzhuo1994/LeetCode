# 1st solution
# O(n) time | O(n) space
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = None
        freq = 0
        for num in cnt:
            if cnt[num] > freq:
                freq = cnt[num]
                ans = num
        return ans