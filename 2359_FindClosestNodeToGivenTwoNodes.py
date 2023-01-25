# 1st solution
# O(n) time | O(n) space
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dp = [[float("inf"), float("inf")] for _ in range(n)]
        dp[node1][0] = 0
        dp[node2][1] = 0

        def dfs(node, k):
            if edges[node] == -1:
                return
            nextNode = edges[node]
            if dp[nextNode][k] != float("inf"):
                return
            dp[nextNode][k] = dp[node][k] + 1
            dfs(nextNode, k)
        
        dfs(node1, 0)
        dfs(node2, 1)

        maxDistance = float("inf")
        ans = -1
        for node in range(n):
            curDist = max(dp[node])
            if curDist == float("inf"):
                continue
            if curDist < maxDistance:
                maxDistance = curDist
                ans = node
        return ans