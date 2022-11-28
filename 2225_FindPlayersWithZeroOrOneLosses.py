# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        for winner, loser in matches:
            if winner not in players:
                players[winner] = [0, 0]
            players[winner][0] += 1
            if loser not in players:
                players[loser] = [0, 0]
            players[loser][1] += 1
        
        ans = [[], []]
        for player in players:
            if players[player][1] == 0:
                ans[0].append(player)
            if players[player][1] == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans 