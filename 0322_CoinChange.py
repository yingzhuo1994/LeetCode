# 1st solution
# O(mn) time | O(n) space
# where m, n are the coin number and the amount value separately.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for _ in range(amount + 1)]
        table[0] = 0
        for denom in coins:
            for i in range(1, len(table)):
                if denom <= i:
                    table[i] = min(table[i], 1 + table[i - denom])
        return -1 if table[-1] == float('inf') else table[-1]

# 2nd solution, BFS
# O(mn) time | O(n) space
# where m, n are the coin number and the amount value separately.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        level = [0]
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while level:
            nc += 1
            newLevel = []
            for v in level:
                for coin in coins:
                    newval = v + coin
                    if newval <= amount and not visited[newval]:
                        if newval == amount:
                            return nc
                        visited[newval] = True
                        newLevel.append(newval)
            level = newLevel
        return -1