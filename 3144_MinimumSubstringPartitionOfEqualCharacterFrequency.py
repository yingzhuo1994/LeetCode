# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float("inf") for _ in range(n + 1)]
        dp[-1] = 0
        for i in range(n):
            dic = {}
            max_cnt = 0
            for j in range(i, n):
                dic[s[j]] = dic.get(s[j], 0) + 1
                max_cnt = max(max_cnt, dic[s[j]])
                if j - i + 1 == max_cnt * len(dic):
                    dp[j] = min(dp[j], dp[i - 1] + 1)
        return dp[n-1]