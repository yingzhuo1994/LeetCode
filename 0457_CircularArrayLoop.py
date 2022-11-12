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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def move(i):
            step = nums[i]
            return (i + step) % n
        
        for i in range(n):
            if nums[i] > 0:
                nums[i] %= n
            else:
                nums[i] = -(abs(nums[i]) % n)

        for i, num in enumerate(nums):
            if abs(num) >= n:
                continue
            linkLength = 0
            j = i
            direction = nums[j]
            while True:
                if direction * nums[j] < 0:
                    break
                if nums[j] > 0:
                    nums[j] += n
                else:
                    nums[j] -= n
                nextj = move(j)
                if nextj == j:
                    break
                j = nextj
                linkLength += 1
                if linkLength > n:
                    return True
        return False