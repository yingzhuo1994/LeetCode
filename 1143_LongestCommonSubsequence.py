class Solution:
    # 1st solution, TLE
    # O(2^(m + n)) time | O(2^(m + n)) space 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans = [0]
        self.dfs(text1, text2, 0, 0, 0, ans)
        return ans[0]
    
    def dfs(self, s1, s2, i, j, curLength, ans):
        if i == len(s1) or j == len(s2):
            ans[0] = max(ans[0], curLength)
            return 
        if s1[i] == s2[j]:
            self.dfs(s1, s2, i + 1, j + 1, curLength + 1, ans)
        else:
            self.dfs(s1, s2, i + 1, j, curLength, ans)
            self.dfs(s1, s2, i, j + 1, curLength, ans)

    # 2nd solution, TLE
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[False for _ in text2] for _ in text1]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = True
        ans = [0]
        self.dfs(dp, 0, 0, 0, ans)
        return ans[0]

    def dfs(self, dp, i, j, curLength, ans):
        if i == len(dp) or j == len(dp[0]):
            ans[0] = max(ans[0], curLength)
            return
        
        for x in range(i, len(dp)):
            for y in range(j, len(dp[0])):
                if dp[x][y]:
                    self.dfs(dp, x + 1, y + 1, curLength + 1, ans)
                else:
                    self.dfs(dp, x + 1, y, curLength, ans)
                    self.dfs(dp, x, y + 1, curLength, ans)

    # 3rd solution, bfs solution
    # O(m*n) time | O(m*n) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[False for _ in text2] for _ in text1]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = True
        ans = 0
        visited = set()
        stack = deque([(0, 0, 0)])
        while stack:
            x, y, length = stack.popleft()
            if x == len(dp) or y == len(dp[0]):
                ans = max(ans, length)
                continue
            if ans == max(len(text1), len(text2)):
                break
            if (x, y) not in visited:
                if dp[x][y]:
                    stack.append((x + 1, y + 1, length + 1))
                else:
                    stack.append((x, y + 1, length))
                    stack.append((x + 1, y, length))
                visited.add((x, y))
        return ans

    # 4th solution, dynamic programming
    # O(mn) time | O(mn) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
