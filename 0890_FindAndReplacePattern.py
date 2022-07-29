# 1st solution
# O(pn) time | O(pn) space
# where n is the length of words, and p is the length of pattern
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if self.isMatch(pattern, word):
                ans.append(word)
        return ans
    
    def isMatch(self, pattern, word):
        pToW = {}
        wToP = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = word[i]
            if p in pToW:
                if pToW[p] != w:
                    return False
            elif w in wToP:
                if wToP[w] != p:
                    return False
            else:
                pToW[p] = w
                wToP[w] = p
        return True
