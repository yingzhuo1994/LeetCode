# 1st solution
# O(n) time | O(1) space
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        count = [0 for _ in range(32)]
        for i in range(32):
            for num in nums:
                count[i] += (num >> i) & 1
        ans = 0
        for i in range(32):
            if count[i] >= k:
                ans |= 1 << i
        return ans