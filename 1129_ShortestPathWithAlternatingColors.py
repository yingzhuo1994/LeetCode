# 1st solution
# O(n) time | O(n) space
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = [[] for _ in range(n)]
        blueGraph = [[] for _ in range(n)]

        for a, b in redEdges:
            redGraph[a].append(b)
        
        for a, b in blueEdges:
            blueGraph[a].append(b)
        
        ans = [float("inf")] * n
        # node, edge
        red_level = [[0, 0]]
        blue_level = [[0, 0]]
        red_set = set([0])
        blue_set = set([0])
        step = 0

        while red_level or blue_level:
            red_stack = []
            blue_stack = []
            for node, step in red_level:
                ans[node] = min(ans[node], step)
                for neib in redGraph[node]:
                    if neib in blue_set:
                        continue
                    blue_stack.append([neib, step + 1])
                    blue_set.add(neib)
            
            for node, step in blue_level:
                ans[node] = min(ans[node], step)
                for neib in blueGraph[node]:
                    if neib in red_set:
                        continue
                    red_stack.append([neib, step + 1])
                    red_set.add(neib)

            red_level = red_stack
            blue_level = blue_stack
        
        return [step if step != float("inf") else -1 for step in ans]