# 1st solution
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [-1 for _ in range(n)]

        graph = [[] for _ in range(n)]

        for i in range(1, n):
            graph[parents[i]].append(i)

        def dfs(node):
            if len(graph[node]) == 0:
                if nums[node] == 1:
                    ans[node] = 2
                else:
                    ans[node] = 1

                return [[nums[node], nums[node]]]
            
            stack = [[[nums[node], nums[node]]]]
            for child in graph[node]:
                stack.append(dfs(child))
            
            interval = mergeIntervals(stack)
            if interval[0][0] != 1:
                ans[node] = 1
            else:
                ans[node] = interval[0][1] + 1

            return interval
        
        def mergeIntervals(stack):
            m = len(stack)
            k = 1
            while k < m:
                for i in range(0, m - k, 2 * k):
                    stack[i] = mergeTwoInterval(stack[i], stack[i + k])
                k *= 2 
            return stack[0]
        
        def mergeTwoInterval(lst1, lst2):
            interval = []
            i, j = 0, 0
            while i < len(lst1) and j < len(lst2):
                if lst1[i][1] + 1 < lst2[j][0]:
                    new = lst1[i]
                    i += 1
                elif lst2[j][1] + 1 < lst1[i][0]:
                    new = lst2[j]
                    j += 1
                else:
                    new = [min(lst1[i][0], lst2[j][0]), max(lst1[i][1], lst2[j][1])]
                    i += 1
                    j += 1
                
                while interval and interval[-1][1] + 1 >= new[0]:
                    new[0] = min(interval[-1][0], new[0])
                    new[1] = max(interval[-1][1], new[1])
                    interval.pop()
                interval.append(new)

            left = lst1 if i < len(lst1) else lst2

            for new in left:
                if interval[-1][1] + 1 < new[0]:
                    interval.append(new)
                else:
                    interval[-1][1] = max(interval[-1][1], new[1])

            return interval
            
        dfs(0)
        return ans