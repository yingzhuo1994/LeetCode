# 1st solution, TLE
# O(3^(m + n)) time | O(m + n) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j, count):
            if i == len(word1) and j == len(word2):
                return count
            if j == len(word2):
                return count + len(word1) - i
            if i == len(word1):
                return count + len(word2) - j

            ans = float("inf")

            if word1[i] == word2[j]:
                ans = min(ans, dfs(i + 1, j + 1, count))
            else:
                ans = min(ans, dfs(i, j + 1, count + 1), dfs(i + 1, j + 1, count + 1), dfs(i + 1, j, count + 1))
            return ans
        return dfs(0, 0, 0)

# 2nd solution
# O((m + n) * mn) time | O(mn) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        level = {(0, 0): 0}
        ans = float("inf")
        while level:
            if (m, n) in level:
                ans = min(ans, level[(m, n)])
            newLevel = {}
            for i, j in level:
                if level[(i, j)] >= ans:
                    continue
                if i == m:
                    newLevel[(m, n)] = min(newLevel.get((m, n), float("inf")), level[(i, j)] + n - j)
                elif j == n:
                    newLevel[(m, n)] = min(newLevel.get((m, n), float("inf")), level[(i, j)] + m - i)
                else:
                    if word1[i] == word2[j]:
                        newLevel[(i + 1, j + 1)] = min(newLevel.get((i + 1, j + 1), float("inf")), level[(i, j)])
                    else:
                        newLevel[(i, j + 1)] = min(newLevel.get((i, j + 1), float("inf")), level[(i, j)] + 1)
                        newLevel[(i + 1, j + 1)] = min(newLevel.get((i + 1, j + 1), float("inf")), level[(i, j)] + 1)
                        newLevel[(i + 1, j)] = min(newLevel.get((i + 1, j), float("inf")), level[(i, j)] + 1)
            level = newLevel
        return ans

# 3rd solution
# O(mn) time | O(mn) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j  # Need to insert `j` chars to become s2[:j]
                elif j == 0:
                    dp[i][j] = i  # Need to delete `i` chars to become ""
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]