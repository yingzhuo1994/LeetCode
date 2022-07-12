class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        N = len(matchsticks)
        matchsticks.sort(reverse = True)

        basket, rem = divmod(sum(matchsticks), k)
        if rem or matchsticks[0] > basket: return False

        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                neib = dp[mask ^ (1<<j)]
                if mask & (1<<j) and neib >= 0 and neib + matchsticks[j] <= basket:
                    dp[mask] = (neib + matchsticks[j]) % basket
                    break

        return dp[-1] == 0
       
