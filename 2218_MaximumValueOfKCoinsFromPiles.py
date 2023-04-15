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