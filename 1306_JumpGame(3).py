# 1st solution
# O(n) time | O(n) space
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = collections.deque([start])
        visited = set()
        while stack:
            node = stack.popleft()
            if arr[node] == 0:
                return True
            nextNodes = [node + arr[node], node - arr[node]]
            for nextNode in nextNodes:
                if nextNode < 0 or nextNode >= len(arr):
                    continue
                if nextNode not in visited:
                    stack.append(nextNode)
                    visited.add(nextNode)
        return False