# 1st solution
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = {}
        for i, route in enumerate(routes):
            for station in route:
                if station not in graph:
                    graph[station] = []
                graph[station].append(i)
        
        stack = [source]
        visitedBus = set()
        vistied = set(stack)
        ans = 1
        while stack:
            newStack = []
            for station in stack:
                for bus in graph[station]:
                    if bus in visitedBus:
                        continue
                    for nextStation in routes[bus]:
                        if nextStation == target:
                            return ans
                        if nextStation in vistied:
                            continue
                        newStack.append(nextStation)
                    visitedBus.add(bus)
            ans += 1
            stack = newStack
        return -1