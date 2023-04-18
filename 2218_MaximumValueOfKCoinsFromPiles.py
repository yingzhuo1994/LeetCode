# 1st solution, TLE
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        key = tuple([0 for _ in range(n + 1)])
        level = set([key])
        for _ in range(k):
            newLevel = set()
            for key in level:
                for i in range(n):
                    idx = key[i]
                    if idx == len(piles[i]):
                        continue
                    lst = list(key)
                    lst[-1] += piles[i][idx]
                    lst[i] += 1
                    newKey = tuple(lst)
                    newLevel.add(newKey)

            level = newLevel
        
        ans = 0
        for key in level:
            ans = max(ans, key[-1])
        return ans

# 2nd solution
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def dfs(idx, left):
            if idx == n:
                if left == 0:
                    return 0
                if left > 0:
                    return float("-inf")
            ans = dfs(idx + 1, left)
            curSum = 0
            for i in range(min(left, len(piles[idx]))):
                curSum += piles[idx][i]
                ans = max(ans, curSum + dfs(idx + 1, left - i - 1))
            return ans
        
        return dfs(0, k)

# 3rd solution
# O(Mk) time | O(k) space
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        dp1 = [0] * (k + 1)
        for lt in piles:
            take = 0
            for i, x in enumerate(lt):
                take += x
                for j in reversed(range(i + 1, k + 1)):
                    dp[j] = max(dp[j], dp1[j - (i + 1)] + take)
            dp1 = dp[:]
        return dp[-1]