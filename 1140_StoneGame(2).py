# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dic = {}
        def dfs(idx, M, player):
            key = (idx, M, player)
            if key in dic:
                return dic[key]
            left = n - idx
            if left <= 2 * M:
                if player == 1:
                    dic[key] = [sum(piles[idx:]), 0]
                else:
                    dic[key] = [0, sum(piles[idx:])]
                return dic[key]
            
            ans = [0, 0]

            for X in range(1, 2 * M + 1):
                end = idx + X
                if player == 1:
                    A, B = dfs(end, max(M, X), -player)
                    Alice = A + sum(piles[idx:end])
                    Bob = B
                    if Alice > ans[0]:
                        ans = [Alice, Bob]
                else:
                    A, B = dfs(end, max(M, X), -player)
                    Alice = A
                    Bob = B + sum(piles[idx:end])
                    if Bob > ans[1]:
                        ans = [Alice, Bob]

            dic[key] = ans
            return ans
        
        ans = dfs(0, 1, 1)[0]
        return ans