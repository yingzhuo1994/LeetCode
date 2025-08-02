# 1st solution
# O(S) time | O(S) space
# where S is the sum of the routes
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
        
        if source not in graph or target not in graph:
            return -1
        
        stack = [source]
        visitedBus = set()
        visitedStation = set(stack)
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
                        if nextStation in visitedStation:
                            continue
                        newStack.append(nextStation)
                        visitedStation.add(nextStation)
                    visitedBus.add(bus)
            ans += 1
            stack = newStack
        return -1