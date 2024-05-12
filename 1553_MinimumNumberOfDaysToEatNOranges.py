# 1st solution, TLE
# O(n) time | O(n) space
class Solution:
    def minDays(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            if i * 2 <= n:
                dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            if i * 3 <= n:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        return dp[n]


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def minDays(self, n: int) -> int:
        visited = set()
        level = set([n])
        day = 0
        while level:
            day += 1
            newLevel = set()
            candidates = []
            for val in level:
                candidates.append(val - 1)
                if val % 2 == 0:
                    new = val // 2
                    candidates.append(new)
                if val % 3 == 0:
                    new = val // 3
                    candidates.append(new)
            for new in candidates:
                if new in visited:
                    continue
                if new == 0:
                    return day
                visited.add(new)
                newLevel.add(new)
            level = newLevel