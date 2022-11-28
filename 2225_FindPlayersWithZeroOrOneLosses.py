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

# 2nd solution
# O(n) time | O(n) space   
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1

        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer