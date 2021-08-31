from typing import Collection


class Solution:
    # 1st solution
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

    # 2nd solution
    # O(n) time | O(k) space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, n, ans = deque([0]), len(nums), []

        for i in range(n):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            
            ans.append(nums[deq[0]])
            
        return ans[k-1:]