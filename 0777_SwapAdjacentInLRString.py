# 1st solution
# O(n) time | O(n) space
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s_count = Counter(start)
        e_count = Counter(end)
        for ch in "LRX":
            if s_count[ch] != e_count[ch]:
                return False
        
        def dfs(s, t):
            if len(s) <= 1:
                return s == t
            if s[0] == t[0]:
                return dfs(s[1:], t[1:])

            if t[0] == "L":
                for i in range(len(s)):
                    if s[i] == "X":
                        continue
                    if s[i] == "L":
                        return dfs(s[:i] + s[i+1:], t[1:])
                    return False
            elif t[0] == "X":
                for i in range(len(s)):
                    if s[i] == "R":
                        continue
                    if s[i] == "X":
                        return dfs(s[:i] + s[i+1:], t[1:])
                    return False
            return False
        
        return dfs(start, end)


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        if start.replace('X', '') != target.replace('X', ''): 
            return False
        j = 0
        for i, c in enumerate(start):
            if c == 'X':
                continue
            
            while target[j] == 'X':
                j += 1
            
            if i != j and (c == 'L') != (i > j):
                return False
            
            j += 1
        return True