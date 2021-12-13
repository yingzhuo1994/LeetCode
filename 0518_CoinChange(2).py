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
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]