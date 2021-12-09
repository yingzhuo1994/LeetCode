# 1st solution
# O(n) time | O(n) space
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = collections.deque([start])
        visited = [False for _ in arr]
        while stack:
            node = stack.popleft()
            nextNodes = [node + arr[node], node - arr[node]]
            for nextNode in nextNodes:
                if nextNode < 0 or nextNode >= len(arr):
                    continue
                if arr[nextNode] == 0:
                    return True
                if not visited[nextNode]:
                    stack.append(nextNode)
                    visited[nextNode] = True
        return False