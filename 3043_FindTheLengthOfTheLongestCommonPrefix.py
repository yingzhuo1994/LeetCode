# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        tier1 = Tier()
        for num in arr1:
            tier1.add(str(num))
        
        tier2 = Tier()
        for num in arr2:
            tier2.add(str(num))
        
        def dfs(t1, t2):
            ans = 0
            for ch in t1:
                if ch in t2:
                    length = dfs(t1[ch], t2[ch]) + 1
                    ans = max(ans, length)
            return ans
        
        return dfs(tier1.root, tier2.root)


class Tier:
    def __init__(self):
        self.root = {}
    
    def add(self, s):
        dic = self.root
        for ch in s:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]

# 2nd solution
# O(m + n) time | O(m) space
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        tier1 = Tier()
        for num in arr1:
            tier1.add(str(num))
        ans = 0
        for num in arr2:
            ans = max(ans, tier1.query(str(num)))
        return ans


class Tier:
    def __init__(self):
        self.root = {}
    
    def add(self, s):
        dic = self.root
        for ch in s:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
    
    def query(self, s):
        dic = self.root
        length = 0
        for ch in s:
            if ch not in dic:
                break
            dic = dic[ch]
            length += 1
        return length