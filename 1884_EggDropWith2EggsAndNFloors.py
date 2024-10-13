# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, len(f)):
            f[i] = min(max(j, f[i - j] + 1) for j in range(1, i + 1))
        return f[n]