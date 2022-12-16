# 1st solution, BFS
# O(n^2) time | O(n^2) space
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        elif jug2Capacity + jug2Capacity == targetCapacity:
            return True
        if jug1Capacity == jug2Capacity:
            return targetCapacity == jug1Capacity
        if jug1Capacity > jug2Capacity:
            jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
        
        stack = deque([[0, 0]])
        visited = set([(0, 0)])
        while stack:
            x, y = stack.popleft()
            if x + y == targetCapacity:
                return True
            if x > 0 and (0, y) not in visited:
                stack.append([0, y])
                visited.add((0, y))
            if y > 0 and (x, 0) not in visited:
                stack.append([x, 0])
                visited.add((x, 0))
            if (jug1Capacity, y) not in visited:
                stack.append([jug1Capacity, y])
                visited.add((jug1Capacity, y))
            if (x, jug2Capacity) not in visited:
                stack.append([x, jug2Capacity])
                visited.add((x, jug2Capacity))
            if x + y > jug2Capacity:
                pair = (x + y - jug2Capacity, jug2Capacity)
            else:
                pair = (0, x + y)
            if pair not in visited:
                stack.append(pair)
                visited.add(pair)

            if x + y > jug1Capacity:
                pair = (jug1Capacity, x + y - jug1Capacity)
            else:
                pair = (x + y, 0)
            if pair not in visited:
                stack.append(pair)
                visited.add(pair)

        return False