class Solution:
    # 1st solution, brute-force, TLE
    # O(mn * 4 ^ (mn)) time | O(1) space
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path = [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, 0, float('-inf'), max_path)
        return max_path[0]
    
    def dfs(self, matrix, i, j, count, last_num, max_path):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])\
            and matrix[i][j] != '#' and matrix[i][j] > last_num:
            count += 1
            max_path[0] = max(count, max_path[0])
            num = matrix[i][j]
            matrix[i][j] = '#'
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                self.dfs(matrix, i + x, j + y, count, num, max_path)
            matrix[i][j] = num