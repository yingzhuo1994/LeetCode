class Solution:
    # 1st solution
    # O(n^2m) time | O(n^2) space
    # where m is average length of word
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