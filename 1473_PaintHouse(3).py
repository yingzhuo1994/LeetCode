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
        for i, oldColor in enumerate(houses):
            for curColor in (range(1, n + 1) if oldColor == 0 else [oldColor]):
                curCost = cost[i][curColor - 1] if curColor != oldColor else 0
                for color, count in dp:
                    curCount = count + (color != curColor)
                    if curCount > target: continue
                    dp2[curColor, curCount] = min(
                        dp2.get((curColor,curCount), float('inf')), 
                        dp[color, count] + curCost)
            dp, dp2 = dp2, {}
        return min([dp[color, count] for color, count in dp if count == target] or [-1])