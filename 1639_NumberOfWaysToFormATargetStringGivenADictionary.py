# 1st solution
# O(mn) time | O(mn) space
# where m = len(target), and n = len(words[0])
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(target)
        n = len(words[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        countDic = [Counter([words[j][k] for j in range(len(words))]) for k in range(n)]

        for j in range(n):
            dp[0][j] = countDic[j][target[0]]
        
        for i in range(1, m):
            curSum = 0
            for j in range(i, n):
                count = countDic[j][target[i]]
                curSum += dp[i - 1][j - 1]
                dp[i][j] = curSum * count % MOD
        
        ans = sum(dp[-1]) % MOD
        return ans

# 2nd solution
# O(s * (w + n)) time | O(n + s) space
# where n = len(target), w = len(words), and s = len(words[0])
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, MOD = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = collections.Counter(word[i] for word in words)
            for j in reversed(range(n)):
                res[j + 1] += res[j] * count[target[j]] % MOD
        return res[n] % MOD