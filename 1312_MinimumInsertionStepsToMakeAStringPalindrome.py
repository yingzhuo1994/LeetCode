# 1st solution
class Solution:
    @cache
    def minInsertions(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        if s[0] == s[-1]:
            return self.minInsertions(s[1:-1])
        left = self.minInsertions(s[1:])
        right = self.minInsertions(s[:-1])
        ans = min(left, right) + 1
        return ans

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = [[s, 0]]
        visited = set([s])
        ans = len(s)
        while stack:
            newStack = []
            for t, count in stack:
                if len(t) <= 1:
                    ans = min(ans, count)
                    continue
                if t[0] == t[-1]:
                    newT = t[1:-1]
                    if newT not in visited:
                        visited.add(newT)
                        newStack.append([newT, count])
                else:
                    for newT in [t[1:], t[:-1]]:
                        if newT in visited:
                            continue
                        visited.add(newT)
                        newStack.append([newT, count + 1])
            stack = newStack
        return ans

# 3rd solution
# O(n^2) time | O(n^2) space
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                # ~j = -j - 1
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]