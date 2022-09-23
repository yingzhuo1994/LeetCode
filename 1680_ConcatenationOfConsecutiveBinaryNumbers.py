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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        for i in range(1, n + 1):
            ans = (ans * (1 << (len(bin(i)) - 2)) + i) % MOD
        return ans