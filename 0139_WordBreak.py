class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]

    # 2nd solution
    # O(n^2) time | O(n) space
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if check[j] and s[j:i] in wordDict:
                    check[i] = True
                    continue
        return check[-1]