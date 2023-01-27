# 1st solution, DFS
# O(n) time | O(n) space
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dp = [[float("inf"), float("inf")] for _ in range(n)]
        dp[node1][0] = 0
        dp[node2][1] = 0

        def dfs(node, k):
            nextNode = edges[node]
            if nextNode == -1:
                return
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

# 2nd solution, BFS
# O(n) time | O(n) space
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(startNode, edges, dist):
            n = len(edges)
            q = deque()
            q.append(startNode)

            visit = [False for _ in range(n)]
            dist[startNode] = 0

            while q:
                node = q.popleft()

                if visit[node]:
                    continue

                visit[node] = True
                neighbor = edges[node]
                if neighbor != -1 and not visit[neighbor]:
                    dist[neighbor] = 1 + dist[node]
                    q.append(neighbor)

        n = len(edges)
        dist1 = [float("inf") for _ in range(n)]
        dist2 = [float("inf") for _ in range(n)]

        bfs(node1, edges, dist1)
        bfs(node2, edges, dist2)

        minDistNode = -1
        minDistTillNow = float("inf")
        for currNode in range(n):
            if minDistTillNow > max(dist1[currNode], dist2[currNode]):
                minDistNode = currNode
                minDistTillNow = max(dist1[currNode], dist2[currNode])

        return minDistNode