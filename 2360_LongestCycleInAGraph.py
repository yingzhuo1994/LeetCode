# 1st solution, TLE
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cycleSet = set()
        n = len(edges)
        ans = -1
        for i in range(n):
            if i in cycleSet:
                continue
            slow = i
            fast = i
            # print(i)
            foundCycle = False
            while fast >= 0 and edges[fast] >= 0:
                slow = edges[slow]
                fast = edges[fast]
                fast = edges[fast]
                # print(slow, fast)
                if slow == fast:
                    foundCycle = True
                    break
            if foundCycle:
                # print("find cycle")
                count = 0
                while slow not in cycleSet:
                    count += 1
                    cycleSet.add(slow)
                    slow = edges[slow]
                ans = max(ans, count)
        return ans

# 2nd solution
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        self.max_length = -1
        seen = [False] * n
        visiting = {}
        stack = []
            
        def dfs(node):
            if not seen[node]:
                if node in visiting:
                    self.max_length = max(self.max_length, len(stack) - visiting[node])
                elif edges[node] != -1: 
                    visiting[node] = len(stack) 
                    stack.append(node)
                    dfs(edges[node])
                    stack.pop()
                    visiting.pop(node)
                seen[node] = True
    
        for i in range(n):            
            dfs(i)
        return self.max_length