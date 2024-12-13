# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findScore(self, nums: List[int]) -> int:
        minHeap = []
        for i, num in enumerate(nums):
            heappush(minHeap, [num, i])
        visited = set()
        score = 0
        while minHeap:
            num, idx = heappop(minHeap)
            if idx not in visited:
                score += num
                visited.add(idx)
                visited.add(idx - 1)
                visited.add(idx + 1)
        return score