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
