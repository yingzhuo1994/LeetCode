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