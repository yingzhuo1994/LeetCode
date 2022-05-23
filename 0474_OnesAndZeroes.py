# 1st solution
# O(kmn) time | O(kmn) space
# where k is the length of strs
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        countArray = [(s.count("0"), s.count("1")) for s in strs]
        
        level = {(m, n): set()}
        length = 0
        while level:
            newLevel = defaultdict(set)
            for i, pair in enumerate(countArray):
                for keyPair, vSet in level.items():
                    if i not in vSet and pair[0] <= keyPair[0] and pair[1] <= keyPair[1]:
                        newPair = (keyPair[0] - pair[0], keyPair[1] - pair[1])
                        if newPair not in newLevel:
                            newLevel[newPair] = vSet.copy()
                            newLevel[newPair].add(i)
            if len(newLevel) == 0:
                return length
            level = newLevel
            length += 1

# 2nd solution
# O(mnk) time | O(mnk) space
# where k is the length of strs
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        
        def dp(mm, nn, kk):
            if mm < 0 or nn < 0: return -float("inf")
            if kk == len(strs): return 0
            x, y = xy[kk]
            return max(1 + dp(mm-x, nn-y, kk + 1), dp(mm, nn, kk + 1))
        
        return dp(m, n, 0)

# 2nd solution
# O(kmn) time | O(mn) space
# where k is the length of strs
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        xy = [[s.count("0"), s.count("1")] for s in strs]
        
        for z, o in xy:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
        return dp[m][n]