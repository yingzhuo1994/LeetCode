# 1st solution
# O(n) time | O(n) space
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def countLowerXOR(array, x):
            count = Counter(array)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2
        return countLowerXOR(nums, high + 1) - countLowerXOR(nums, low)