# 1st solution
# O(n) time | O(n) space
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def move(i):
            step = nums[i]
            return (i + step) % n
        
        visited = set()
        for i in range(n):
            if i not in visited:
                idx = i
                newVisited = set()
                while idx not in newVisited:
                    newVisited.add(idx)
                    idx = move(idx)
                if idx in visited:
                    visited = visited.union(newVisited)
                    continue
                visited = visited.union(newVisited)

                cycleVisited = set()
                direction = nums[idx]
                isValid = True
                while idx not in cycleVisited:
                    cycleVisited.add(idx)
                    idx = move(idx)
                    if nums[idx] * direction < 0:
                        isValid = False
                        break

                if isValid and len(cycleVisited) > 1:
                    return True
        return False

