from typing import Collection


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        hp = []
        for i in range(k):
            heapq.heappush(hp, [-nums[i], i])
        res.append(-hp[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(hp, [-nums[i], i])
            while hp[0][1] <= i - k:
                heapq.heappop(hp)
            res.append(-hp[0][0])
        return res