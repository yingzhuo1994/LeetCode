# 1st solution
# O(n) time | O(n) space
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        stack = []
        for i in range(1, n + 1):
            stack.append(bin(i)[2:])
        ans = "".join(stack)
        ans = int(ans, 2) % MOD
        return ans
        