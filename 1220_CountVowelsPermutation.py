# 1st solution, BFS
# O(5^n) time | O(1) space
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
