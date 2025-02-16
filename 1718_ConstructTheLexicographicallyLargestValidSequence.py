# 1st solution
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        visited = [False] * (n + 1)

        def dfs(i):
            if i == len(ans):
                return True
            if ans[i] != 0:
                return dfs(i + 1)
            for num in range(n, 0, -1):
                if visited[num]:
                    continue
                if num == 1:
                    ans[i] = 1
                    visited[1] = True
                    if dfs(i + 1):
                        return True
                    visited[1] = False
                    ans[i] = 0
                else:
                    j = i + num
                    if j >= len(ans):
                        continue
                    if ans[j] == 0:
                        ans[i] = num
                        ans[j] = num
                        visited[num] = True
                        if dfs(i + 1):
                            return True
                        visited[num] = False
                        ans[i] = 0
                        ans[j] = 0
            return False
        dfs(0)
        return ans