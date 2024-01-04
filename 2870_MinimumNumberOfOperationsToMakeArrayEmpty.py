# 1st solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for freq in count.values():
            if freq == 1:
                return -1
            q, r = divmod(freq, 3)
            if r == 0:
                ans += q
            else:
                ans += q + 1
        return ans