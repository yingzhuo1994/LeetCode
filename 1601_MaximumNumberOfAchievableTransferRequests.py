# 1st solution
# O((n + r) * 2^r) time | O(n + r) space
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        total = len(requests)
        idxArray = [j for j in range(total)]
        for i in reversed(range(total + 1)):
            for c in itertools.combinations(idxArray, i):
                net = [0 for _ in range(n)]
                for idx in c:
                    net[requests[idx][0]] -= 1
                    net[requests[idx][1]] += 1
                if net == [0 for j in range(n)]:
                    return i
        return 0

# 2nd solution
# O(r * (r + n)) time | O(r + n) space
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        s = n # source index
        t = n + 1 # target index
        N = n + 2 # total vertex number including a source and a target
        K = 0

        # calculate the diff array
        diff = [0 for _ in range(n)]
        for a, b in requests:
            diff[a] += 1
            diff[b] -= 1

        # create the edges
        edges = []
        for i in range(n):
            if diff[i] > 0:
                for _ in range(diff[i]):
                    edges.append(Edge(s, i, 0))
            elif diff[i] < 0:
                for _ in range(-diff[i]):
                    edges.append(Edge(i, t, 0))
    
            K += max(diff[i], 0)
        
        for a, b in requests:
            edges.append(Edge(a, b, 1))

        # build the graph
        G = [[] for _ in range(N)]
        for i in range(len(edges)):
            G[edges[i].s].append(i)
            G[edges[i].t].append(i)
        
        ans = len(requests)
        # using ssp algorithm with 01BFS to find the min-cost max-flow
        h = [0 for _ in range(N)]
        for k in range(K):
            distance = [N for _ in range(N)]
            pre = [-1 for _ in range(N)]
            done = [0 for _ in range(N)]

            distance[s] = 0
            q = deque()
            q.appendleft(s)
            while q:
                u = q.popleft()
 
                if done[u]:
                    continue

                done[u] = 1
                for i in G[u]:
                    if edges[i].s == u:
                        w = edges[i].cost + h[u] - h[edges[i].t]
                        if distance[edges[i].t] > distance[u] + w:
                            distance[edges[i].t] = distance[u] + w
                            if w:
                                q.append(edges[i].t)
                            else:
                                q.appendleft(edges[i].t)
                            pre[edges[i].t] = i

            for i in range(N):
                h[i] += distance[i]
            
            ans -= h[t]

            u = t
            while u != s:
                edges[pre[u]].cost = -edges[pre[u]].cost
                edges[pre[u]].s, edges[pre[u]].t = edges[pre[u]].t, edges[pre[u]].s
                u = edges[pre[u]].t

        return ans

class Edge:
    def __init__(self, s, t, cost):
        self.s = s
        self.t = t
        self.cost = cost