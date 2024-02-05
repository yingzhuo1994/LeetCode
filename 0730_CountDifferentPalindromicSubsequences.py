# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for cur_len in range(2, n + 1):  # 从长度为2的子串开始计算
            # 挨个计算长度为len的子串的回文子序列个数
            for i in range(0, n - cur_len + 1):
                j = i + cur_len - 1
                # 情况(1) 相等
                if s[i] == s[j]:
                    l, r = i + 1, j - 1
                    while l <= r and s[l] != s[i]:
                        l += 1
                    while l <= r and s[r] != s[j]:
                        r -= 1
                    if l > r:  # 情况① 没有重复字符
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    elif l == r:  # 情况② 出现一个重复字符
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    else:  # 情况③ 有两个及两个以上
                        dp[i][j] = 2 * dp[i + 1][j - 1] - dp[l + 1][r - 1]
                else:  # 情况(2) 不相等
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                dp[i][j] = dp[i][j] % mod  # Python直接取模也没有问题
        return dp[0][n - 1]
