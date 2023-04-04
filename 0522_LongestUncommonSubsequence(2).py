# 1st solution
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        dp = [Counter() for _ in range(11)]
        for s in strs:
            k = len(s)
            dp[k][s] += 1
        
        visited = set()
        for k in reversed(range(1, 11)):
            for s in dp[k]:
                if dp[k][s] == 1 and s not in visited:
                    return k
                visited.add(s)
            newVisited = set()
            for s in visited:
                for i in range(len(s)):
                    newVisited.add(s[:i] + s[i+1:])
            visited = newVisited
        return -1

# 2nd solution
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
 
        strs.sort(key = lambda x: -len(x))
        for i, word in enumerate(strs):
            if all(not isSubsequence(word, strs[j]) for j in range(len(strs)) if j != i): 
                return len(word)
        
        return -1

# 3rd solution
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(w1, w2, idx):
            for ch in w2:
                if ch == w1[idx]:
                     idx += 1
                if idx == len(w1): 
                    return True 
            return False
        
        dic = collections.Counter(strs)
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            if dic[strs[i]] == 1:
                res = any(isSub(strs[i], strs[j], 0) for j in range(i))        
                if res == False: 
                    return len(strs[i])
        return -1