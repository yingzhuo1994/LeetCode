# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, len(f)):
            f[i] = min(max(j, f[i - j] + 1) for j in range(1, i + 1))
        return f[n]


# 2nd solution
# O(1) time | O(1) space
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((sqrt(n * 8 + 1) - 1) / 2)