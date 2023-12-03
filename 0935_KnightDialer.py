# 1st solution
# O(n) time | O(n) space
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dic = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        @cache
        def dfs(node, step):
            if step == 0:
                return 1
            ans = 0
            for neig in dic[node]:
                ans += dfs(neig, step - 1)
            ans %= MOD
            return ans
            
        ans = 0
        for i in range(10):
            ans += dfs(i, n - 1)
            ans %= MOD
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7
        dic = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        stack = [1 for _ in range(10)]
        stack[5] = 0
        
        for _ in range(n - 1):
            new = [0 for _ in range(10)]
            for i in dic:
                for neig in dic[i]:
                    new[neig] += stack[i]
                    new[neig] %= MOD
            
            stack = new
        ans = sum(stack) % MOD
        return ans

# 3rd solution
# O(log(n)) time | O(1) space
import numpy as np
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res = 1
        k = n - 1
        while k:
            if k % 2:
                res = res * M % MOD
            M = M * M % MOD
            k //= 2
        return int(np.sum(res)) % MOD