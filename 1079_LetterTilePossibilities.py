# 1st solution
# O(2^n) time | O(2^n) space
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(n, s):
            if len(s) == n:
                seq.add(s)
                return
            for i, ch in enumerate(tiles):
                if visited[i]:
                    continue
                visited[i] = True
                dfs(n, s + ch)
                visited[i] = False
            return
        ans = 0
        for i in range(1, len(tiles) + 1):
            visited = [False] * len(tiles)
            seq = set()
            dfs(i, "")
            ans += len(seq)
        return ans