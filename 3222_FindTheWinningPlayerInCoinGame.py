# 1st solution
# O(n) time | O(1) space
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        b = y // 4
        turn = min(x, b)
        if turn & 1:
            return "Alice"
        else:
            return "Bob"
