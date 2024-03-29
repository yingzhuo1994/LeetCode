# 1st solution, BFS
# O(n) time | O(1) space
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dic = {"a": ["e"],
               "e": ["a", "i"],
               "i": ["a", "e", "o", "u"],
               "o": ["i", "u"],
               "u": ["a"]}
        level = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        
        length = n
        while length > 1:
            newLevel = {}
            for ch in level:
                for nextCh in dic[ch]:
                    newLevel[nextCh] = newLevel.get(nextCh, 0) + level[ch]
                    newLevel[nextCh] %= MOD
            level = newLevel
            length -= 1

        ans = sum(level.values())
        ans %= MOD
        return ans

# 2nd solution, BFS
# O(n) time | O(1) space
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u= 1, 1, 1, 1, 1
        MOD = 10**9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u)%MOD, (a + i)%MOD, (e + o)%MOD, i%MOD, (i + o)%MOD
        
        return (a + e + i + o + u)%MOD