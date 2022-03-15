# 1st solution
# O(m*log(n)) time | O(n) space
# where n is the length of nums and m is total number of candidates,
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for listIdx, lst in enumerate(nums):
            heap.append([lst[0], listIdx, 0])
        
        Max = max(num for num, listIdx, numIdx in heap)
        heapify(heap)
        ans = [0, float("inf")]

        while len(heap) == len(nums):
            num, listIdx, numIdx = heappop(heap)
            if Max - num < ans[1] - ans[0]:
                ans = [num, Max]
            if numIdx < len(nums[listIdx]) - 1:
                nextNum = nums[listIdx][numIdx + 1]
                heappush(heap, [nextNum, listIdx, numIdx + 1])
                Max = max(Max, nextNum)
            
        return ans