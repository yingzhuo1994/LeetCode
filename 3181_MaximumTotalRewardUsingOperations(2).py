# 1st solution
# O(nm/w) time | O(n + m/w) space
# where n = len(rewardValues), m = max(rewardValues), w = 64 or 32
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        m = max(rewardValues)
        s = set()
        for v in rewardValues:
            if v in s:
                continue
            if v == m - 1 or m - 1 - v in s:
                return m * 2 - 1
            s.add(v)

        f = 1
        for v in sorted(s):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1