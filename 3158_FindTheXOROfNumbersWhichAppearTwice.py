# 1st solution
# O(n) time | O(n) space
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for key in cnt:
            if cnt[key] == 2:
                ans ^= key
        return ans