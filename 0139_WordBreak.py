# 1st solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if check[j] and s[j:i] in wordDict:
                    check[i] = True
                    continue
        return check[-1]

# 3rd solution
# O(n^2) time | O(n) space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for start in range(len(dp)):
            if dp[start]:
                for end in range(start + 1, len(dp)):
                    if s[start:end] in wordSet:
                        dp[end] = True
                if dp[-1]:
                    return True
        return dp[-1]