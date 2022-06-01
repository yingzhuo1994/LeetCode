# 1st solution
# O(n^2m) time | O(n^2) space
# where m is average length of word
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        dp_solution = [[] for _ in range(n)] + [[""]]
        dp = [0] * n + [1]
        
        for k in range(n):
            for j in range(k,-1,-1):
                if s[j: k + 1] in wordSet:
                    dp[k] = max(dp[k], dp[j-1])

        if dp[-2] == 0: return []

        for k in range(n):
            for j in range(k,-1,-1):
                if s[j: k + 1] in wordSet:
                    for sol in dp_solution[j-1]:
                        dp_solution[k].append(sol + " " + s[j: k + 1])
                        
        return [seq[1:] for seq in dp_solution[-2]]

# 2nd solution
# O(n^2m) time | O(n^2) space
# where m is average length of word
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True
        for i in range(len(s)):
            for j in range(i + 1):
                if dp[j - 1] and s[j:i + 1] in wordSet:
                    dp[i] = True

        if not dp[-2]:
            return []
        res = [[] for _ in range(len(s) + 1)]
        res[-1] = ['']
        for i in range(len(s)):
            for j in range(i+1):
                if s[j: i + 1] in wordSet:
                    res[i].extend([w + ' ' + s[j:i + 1] for w in res[j - 1]])
        return [w[1:] for w in res[-2]]
                    