# 1st solution
# O(m * log(m)) time | O(1) space
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = 0
        ans = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1
        return ans