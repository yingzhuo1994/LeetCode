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

# 3rd solution
# O((log(n))^2) time | O((log(n))^2) space
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def f(k):
            if k <= 1:
                return k
            day = 1 + min((k % 2) + f(k//2), (k % 3) + f(k//3)) 
            return day
        return f(n)

# 4th solution, Dijkstra
# O((log(n))^2 * log(log(n))) time | O((log(n))^2) space
class Solution:
    def minDays(self, n: int) -> int:
        dis = defaultdict(lambda: inf)
        h = [(0, n)]
        while True:
            dx, x = heappop(h)
            if x <= 1:
                return dx + x
            if dx > dis[x]:
                continue
            for d in 2, 3:
                y = x // d
                dy = dx + x % d + 1
                if dy < dis[y]:
                    dis[y] = dy
                    heappush(h, (dy, y))