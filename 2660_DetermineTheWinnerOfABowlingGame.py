# 1st solution
# O(n) time | O(1) space
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def getScore(pins):
            score = 0
            lastDouble = -3
            for i, pin in enumerate(pins):
                if i - lastDouble <= 2:
                    score += 2 * pin
                else:
                    score += pin
                if pin == 10:
                    lastDouble = i
            return score
        
        score1 = getScore(player1)
        score2 = getScore(player2)
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        return 0