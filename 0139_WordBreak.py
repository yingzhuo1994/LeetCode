class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        p1, p2 = 0, 1
        test = False        
        while p2 <= len(s):
            if s[p1:p2] in wordDict:
                test = self.wordBreak(s[p2:], wordDict)
            if test:
                return True
            p2 += 1
        return False