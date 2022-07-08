# 1st solution, TLE
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.ans = float("inf")
        
        def dfs(idx, lastColor, totalCost, count):
            if idx == len(houses):
                if count == target:
                    self.ans = min(self.ans, totalCost)
                return

            if count > target:
                return
            
            if houses[idx] == 0:
                for j in range(n):
                    houses[idx] = j + 1
                    if houses[idx] != lastColor:
                        dfs(idx + 1, houses[idx], totalCost + cost[idx][j], count + 1)
                    else:
                        dfs(idx + 1, houses[idx], totalCost + cost[idx][j], count)
                    houses[idx] = 0
            else:
                if houses[idx] != lastColor:
                    dfs(idx + 1, houses[idx], totalCost, count + 1)
                else:
                    dfs(idx + 1, houses[idx], totalCost, count)
        

        dfs(0, 0, 0, 0)
        return self.ans if self.ans != float("inf") else -1

# 2nd solution, dp
# O(m * n^2 * k) time | O(mnk) space
# where k = target
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = [[[float("inf") for _ in range(target + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        memo[-1][0][0] = 0

        for i in range(m):
            if houses[i] != 0:
                a = i - 1
                j = houses[i]
                for b in range(n + 1):
                    for c in range(1, target + 1):
                        if j == b:
                            memo[i][j][c] = min(memo[i][j][c], memo[a][b][c])
                        else:
                            if c + 1 <= target:
                                memo[i][j][c+1] = min(memo[i][j][c+1], memo[a][b][c])
            else:
                a = i - 1
                for b in range(n + 1):
                    for c in range(1, target + 1):
                        for j in range(1, n + 1):
                            if j == b:
                                memo[i][j][c] = min(memo[i][j][c], memo[a][b][c] + cost[i][j-1])
                            else:
                                if c + 1 <= target:
                                    memo[i][j][c+1] = min(memo[i][j][c+1], memo[a][b][c] + cost[i][j-1])
        
        ans = float("inf")
        for j in range(1, n + 1):
            ans = min(ans, memo[m-1][j][target])

        return ans if ans != float("inf") else - 1

# 3rd solution, dp
# O(m * n^2 * k) time | O(nk) space
# where k = target
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp, dp2 = {(0, 0): 0}, {}
        for i, a in enumerate(houses):
            for cj in (range(1, n + 1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target: continue
                    dp2[cj, b2] = min(dp2.get((cj,b2), float('inf')), dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}
        return min([dp[c, b] for c, b in dp if b == target] or [-1])