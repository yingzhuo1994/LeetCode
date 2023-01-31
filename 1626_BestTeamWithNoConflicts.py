# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [[age, score] for age, score in zip(ages, scores)]
        players.sort()
        n = len(players)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = players[i][1]
            for j in reversed(range(i)):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)

# 2nd solution
# O(n*log(n) + kn) time | O(k) space
# where n = len(scores) and k = max(ages)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [[score, age] for age, score in zip(ages, scores)]
        players.sort()
        k = max(ages)
        dp = [0] * (k + 1)
        
        for score, age in players:
            dp[age] = score + max(dp[:age+1])
        
        return max(dp)