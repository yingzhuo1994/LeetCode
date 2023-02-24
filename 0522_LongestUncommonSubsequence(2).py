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