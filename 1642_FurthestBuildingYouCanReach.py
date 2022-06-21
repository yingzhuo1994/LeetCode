# 1st solution, MLE
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        level = {(bricks, ladders)}
        distance = 0
        curHeight = heights[0]
        for i in range(1, len(heights)):
            diff = heights[i] - curHeight
            if diff > 0:
                newLevel = set()
                for brick, ladder in level:
                    if brick >= diff:
                        newLevel.add((brick-diff, ladder))
                    if ladder > 0:
                        newLevel.add((brick, ladder - 1))
                if not newLevel:
                    break
                level = newLevel
            
            distance += 1
            curHeight = heights[i]
        
        return distance

# 2nd solution, min heap
# O(n*log(n)) time | O(n) space
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        stack = []
        distance = 0
        while distance + 1 < len(heights):
            diff = heights[distance + 1] - heights[distance]
            if diff > 0:
                if bricks - diff >= 0:
                    heapq.heappush(stack, -diff)
                    bricks -= diff
                else:
                    if ladders > 0:
                        if stack:
                            if -stack[0] > diff:
                                bricks += -heapq.heappop(stack) - diff
                                heapq.heappush(stack, -diff)
                        ladders -= 1
                    else:
                        break
            distance += 1
        return distance

# 3rd solution, min heap
# O(n*log(k)) time | O(k) space
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if ladders >= len(heights) - 1:
            return len(heights) - 1
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1