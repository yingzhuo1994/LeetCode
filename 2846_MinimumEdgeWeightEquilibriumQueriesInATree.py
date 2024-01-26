# 1st solution, TLE
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        def find_path(source, target, prev=-1):
            if source == target:
                return [0]
            for neig, weight in graph[source]:
                if neig == prev:
                    continue
                if neig == target:
                    return [weight]
                lst = find_path(neig, target, source)
                if len(lst) > 0:
                    return [weight] + lst
            
            return []
        
        def get_answer(u, v):
            path = find_path(u, v)
            if len(path) > 0:
                count = Counter(path)
                max_freq = max(count.values())
                return len(path) - max_freq
            
            return -1
        
        return [get_answer(u, v) for u, v in queries]