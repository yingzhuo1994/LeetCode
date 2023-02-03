# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        players = [[s, i] for i, s in enumerate(score)]
        players.sort(reverse=True)
        n = len(players)
        ans = [None for _ in range(n)]
        if n >= 1:
            idx = players[0][1]
            ans[idx] = "Gold Medal"

        if n >= 2:
            idx = players[1][1]
            ans[idx] = "Silver Medal"

        if n >= 3:
            idx = players[2][1]
            ans[idx] = "Bronze Medal"
        
        for i in range(3, n):
            idx = players[i][1]
            ans[idx] = str(i + 1)
        
        return ans
