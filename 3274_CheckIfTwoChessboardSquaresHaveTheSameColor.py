# 1st solution
# O(1) time | O(1) space
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a = abs(ord(coordinate1[0]) - ord(coordinate2[0]))
        b = abs(int(coordinate1[1]) - int(coordinate2[1]))
        ans = True
        if a & 1:
            ans = not ans
        if b & 1:
            ans = not ans
        return ans