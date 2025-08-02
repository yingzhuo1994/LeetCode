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


# 2nd solution
# O(n * (m + log(n))) time | O(m + log(n)) space
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        m = rewardValues[-1]
        dp = [0] * (2 * m)
        dp[0] = 1
        for x in rewardValues:
            for k in range(2 * x - 1, x - 1, -1):
                if dp[k - x] == 1:
                    dp[k] = 1
        res = 0
        for i in range(len(dp)):
            if dp[i] == 1:
                res = i
        return res