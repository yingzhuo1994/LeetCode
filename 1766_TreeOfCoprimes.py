# 1st solution
# O(n) time | O(n) space
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        coprimes = [[False for _ in range(51)] for _ in range(51)]
        for a in range(1, 51):
            for b in range(a, 51):
                if gcd(a, b) == 1:
                    coprimes[a][b] = True
                    coprimes[b][a] = True
        
        n = len(nums)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        heights = [-1 for _ in range(n)]
        def getHeight(idx, prev, height):
            heights[idx] = height
            for neig in graph[idx]:
                if neig == prev:
                    continue
                getHeight(neig, idx, height + 1)
        
        getHeight(0, -1, 0)
        
        ans = [-1 for _ in range(n)]
        def dfs(node, parent, dic):
            for num in dic:
                if dic[num] < 0:
                    continue
                if coprimes[num][nums[node]]:
                    if ans[node] == -1 or heights[dic[num]] > heights[ans[node]]:
                        ans[node] = dic[num]

            idx = dic.get(nums[node], -1)
            for neig in graph[node]:
                if neig == parent:
                    continue
                dic[nums[node]] = node
                dfs(neig, node, dic)
                dic[nums[node]] = idx
        dfs(0, -1, {})
        return ans
