# 1st solution
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.dic = {0: False, 1: True}
        winner = self.playInTurn(n, 1)
        return winner == 1

    def playInTurn(self, n, player):
        opponent = -player
        if n in self.dic:
            if self.dic[n]:
                return player
            else:
                return opponent
        k = 1
        while k**2 <= n:
            left = n - k**2
            if left not in self.dic:
                self.dic[left] = self.playInTurn(left, opponent) == opponent
            if not self.dic[left]:
                self.dic[n] = True
                return player
            k += 1
        self.dic[n] = False
        return opponent

# 2nd solution
# O(n*n^0.5) time | O(n) space
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(n+1):
            if dp[i]:
                continue
            for k in range(1, int(n**0.5)+1):
                if i+k*k <= n:
                    dp[i+k*k] = True
                else:
                    break
        return dp[n]