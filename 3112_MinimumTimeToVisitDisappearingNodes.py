# 1st solution
# O(V^2) time | O((V+E) * log(V))
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])
        disappearDic = {}
        for i, t in enumerate(disappear):
            if t not in disappearDic:
                disappearDic[t] = []
            disappearDic[t].append(i)


        validNodes = [True for _ in range(n)]
        visited = [False for _ in range(n)]
        ans = [float("inf") for _ in range(n)]
        ans[0] = 0
        minHeap = [[0, 0]] # time, node
        for t in sorted(disappearDic.keys()):
            lst = disappearDic[t]
            while minHeap and minHeap[0][0] < t:
                t1, node = heappop(minHeap)
                if not validNodes[node] or visited[node]:
                    continue
                visited[node] = True
                for neig, w in graph[node]:
                    if not validNodes[neig] or visited[neig]:
                        continue
                    t2 = t1 + w
                    if t2 < disappear[neig]:
                        ans[neig] = min(ans[neig], t2)
                    if t2 <= ans[neig]:
                        heappush(minHeap, [t2, neig])
                    
            for i in lst:
                validNodes[i] = False
        return [t if t != float("inf") else -1 for t in ans ]
