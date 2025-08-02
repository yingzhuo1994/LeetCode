# 1st solution
# O(n) time | O(1) space
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = (1 << maximumBit) - 1
        ans = []
        cur = reduce(lambda x, y: x ^ y, nums)
        n = len(nums)
        for i in reversed(range(n)):
            ans.append(cur ^  target)
            cur ^= nums[i]
        return ans