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

# 3rd solution
# O((log(n))^2) time | O(log(n)) space
class Solution:
    def concatenatedBinary(self, n: int, p: int = 10 ** 9 + 7) -> int:
        def matmul(X, Y, p):
            return [[sum(a * b for a, b in zip(X_row, Y_col)) % p for Y_col in zip(*Y)] for X_row in X]

        def mv(X, v, p):
            return [sum(a * b for a, b in zip(X_row, v)) % p for X_row in X]

        def matpowv(X, n, v, p):
            while n > 0:
                if n & 1: v = mv(X, v, p)
                X, n = matmul(X, X, p), n >> 1
            return v
    
        n += 1
        v = [0, 1, 1]
        bit = 1
        while bit < n:
            M = bit << 1
            mat = [
                [M, 1, 0],
                [0, 1, 1],
                [0, 0, 1],
            ]
            npow = min(bit, n - bit)
            v = matpowv(mat, npow, v, p)
            bit = M
        return v[0]