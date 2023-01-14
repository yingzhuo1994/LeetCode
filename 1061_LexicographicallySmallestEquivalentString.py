# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        DS = DisjointSet()
        for ch in string.ascii_lowercase:
            DS.add(ch)
        
        for ch1, ch2 in zip(s1, s2):
            DS.merge(ch1, ch2)
        
        ans = []
        for ch in baseStr:
            ans.append(DS.getParent(ch))

        return "".join(ans)

class DisjointSet:
    def __init__(self):
        self.parents = {}
    
    def add(self, ch):
        if ch not in self.parents:
            self.parents[ch] = ch
    
    def merge(self, ch1, ch2):
        p1, p2 = self.getParent(ch1), self.getParent(ch2)
        if p1 > p2:
            ch1, ch2 = ch2, ch1
            p1, p2 = p2, p1
        self.parents[p2] = p1
    
    def getParent(self, ch):
        if ch != self.parents[ch]:
            self.parents[ch] = self.getParent(self.parents[ch])
        return self.parents[ch]