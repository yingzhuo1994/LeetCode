# 1st solution
# O(n) time | O(n) space
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, num in enumerate(arr):
            dic[num].append(i)
        
        visited = set([0])
        level = set([0])
        step = 0
        while level:
            newLevel = set()
            for k in level:
                if k == len(arr) - 1:
                    return step
                if k - 1 >= 0 and k - 1 not in visited:
                    newLevel.add(k - 1)
                    visited.add(k - 1)
                if k + 1 < len(arr) and k + 1 not in visited:
                    newLevel.add(k + 1)
                    visited.add(k + 1)
                for idx in dic[arr[k]]:
                    if idx not in visited:
                        newLevel.add(idx)
                        visited.add(idx)
                dic[arr[k]].clear()
            level = newLevel
            step += 1
        return step

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1