# 1st solution
# O(n) time | O(1) space
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = Counter(secret)
        A = 0
        B = 0
        for a, b in zip(secret, guess):
            if a == b:
                A += 1
                dic[a] -= 1
        for a, b in zip(secret, guess):
            if a != b and dic[b] > 0:
                dic[b] -= 1
                B += 1
        return f"{A}A{B}B"