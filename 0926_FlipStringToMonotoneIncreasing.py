# 1st solution
# O(n) time | O(n) space
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for _ in range(n + 1)]
        for i, ch in enumerate(s):
            dp[i] = dp[i-1][:]
            if ch == "1":
                dp[i][1] += 1
            else:
                dp[i][0] += 1
        
        ans = n
        for i in range(n):
            front = dp[i-1][1]
            back = dp[n-1][0] - dp[i-1][0]
            count = front + back
            ans = min(ans, count)
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros_total = s.count("0")
        ones_total = n - zeros_total

        zero = 0
        one = 0
        ans = min(zeros_total, ones_total)
        for i, ch in enumerate(s):
            if ch == "0":
                zero += 1
            else:
                one += 1

            front = one
            back = zeros_total - zero
            count = front + back

            ans = min(ans, count)
        return ans