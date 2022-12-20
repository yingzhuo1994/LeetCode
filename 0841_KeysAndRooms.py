# 1st solution
# O(n) time | O(n) space
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False for _ in range(n)]
        visited[0] = True
        stack = deque([0])
        while stack:
            room = stack.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        return all(visited)