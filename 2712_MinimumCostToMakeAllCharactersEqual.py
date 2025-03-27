# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        left1 = [0] * (n + 1)
        right1 = [0] * (n + 1)
        left0 = [0] * (n + 1)
        right0 = [0] * (n + 1)
        if s[0] == "0":
            left1[0] = 1
        else:
            left0[0] = 1
        if s[-1] == "0":
            right1[n-1] = 1
        else:
            right0[n-1] = 1
        
        for i in range(1, n):
            if s[i] == "0":
                left0[i] = left0[i-1]
                left1[i] = left0[i-1] + i + 1
            else:
                left0[i] = left1[i-1] + i + 1
                left1[i] = left1[i-1]
        
        for i in reversed(range(n - 1)):
            if s[i] == "0":
                right0[i] = right0[i+1]
                right1[i] = right0[i+1] + n - i
            else:
                right0[i] = right1[i+1] + n - i
                right1[i] = right1[i+1]

        ans = float("inf")
        for i, ch in enumerate(s):
            if int(ch) == 0:
                val0 = left0[i-1] + right0[i+1]
                val1 = min(left1[i] + right1[i+1], left1[i-1] + right1[i])
                ans = min(ans, val0, val1)
            else:
                val0 = min(left0[i-1] + right0[i], left0[i] + right0[i+1])
                val1 = left1[i-1] + right1[i+1]
                ans = min(ans, val0, val1)
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i - 1] != s[i]:
                ans += min(i, n - i)
        return ans