# 1nd solution
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        n = len(s)

        def dp(i, k, last_char, last_len):
            if k < 0:
                return float('inf')
            if i + k >= n:
                return 0
            if (i, k, last_char, last_len) not in memo:
                if s[i] == last_char:
                    carry = last_len in {1, 9, 99}
                    memo[i, k, last_char, last_len] = carry + \
                        dp(i + 1, k, last_char, last_len + 1)
                else:
                    memo[i, k, last_char, last_len] = min(
                        dp(i + 1, k, s[i], 1) + 1,
                        dp(i + 1, k - 1, last_char, last_len))
            return memo[i, k, last_char, last_len]

        return dp(0, k, '', 0)