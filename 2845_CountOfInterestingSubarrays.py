# 1st solution
# O(n) time | O(mod) space
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = acc = 0
        count = Counter({0: 1})
        for a in nums:
            acc = (acc + (1 if a % modulo == k else 0)) % modulo
            res += count[(acc - k) % modulo]
            count[acc] += 1
        return res