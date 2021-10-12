class Solution:
    # 1st solution, brute-force
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minSum = [float('inf')]
        self.dfs(triangle, 0, 0, 0, minSum)
        return minSum[0]
    
    def dfs(self, triangle, layer, index, curSum, minSum):
        if layer == len(triangle) - 1:
            if index < len(triangle[layer]):
                curSum += triangle[layer][index]
                minSum[0] = min(minSum[0], curSum)
            return 
        
        self.dfs(triangle, layer + 1, index, curSum + triangle[layer][index], minSum)
        self.dfs(triangle, layer + 1, index + 1, curSum + triangle[layer][index], minSum)
    
    # 2nd solution, dp
    # O(n) time | O(n) space
    # where n is the element number of triangle
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[value for value in layer] for layer in triangle]
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]