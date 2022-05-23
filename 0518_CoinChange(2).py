# 1st solution, TLE
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = []
        self.dfs(coins, amount, 0, [], ans)
        return len(ans)
    
    def dfs(self, coins, goal, idx, path, ans):
        if goal < 0:
            return 
        if goal == 0:
            ans.append(path)
            return 
        
        for i in range(idx, len(coins)):
            self.dfs(coins, goal - coins[i], i, path + [coins[i]], ans)

# 2nd solution
# O(kn) time | O(n) space
# where k is the number of coins, and n is amount.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for denom in coins:
            for value in range(1, amount + 1):
                if value >= denom:
                    dp[value] += dp[value - denom]
        return dp[amount]