# 1st solution, TLE
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primes = [True for _ in range(n + 1)]
        primes[0] = False
        primes[1] = False
        for i in range(2, n + 1):
            if primes[i]:
                primes[i+i::i] = [False] * len(primes[i+i::i])
        graph = {i: [] for i in range(1, n +1)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, prev=None):
            if not node or primes[node]:
                return 0
            count = 1
            for neig in graph[node]:
                if neig == prev:
                    continue

                count += dfs(neig, node)

            return count
        
        ans = 0
        for node in range(1, n + 1):
            if primes[node]:
                lst = [dfs(neig, node) for neig in graph[node]]
                for i in range(len(lst)):
                    for j in range(i+1, len(lst)):
                        ans += lst[i] * lst[j]
                ans += sum(lst + [0])
        return ans