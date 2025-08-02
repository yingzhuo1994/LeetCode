# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minHeap = []
        maxHeap = []
        ans = 0
        start = 0
        for i, num in enumerate(nums):
            heappush(minHeap, [num, i])
            heappush(maxHeap, [-num, i])
            while True:
                diff = -maxHeap[0][0] - minHeap[0][0]
                if diff <= 2:
                    ans += i - start + 1
                    break
                start += 1
                while maxHeap[0][1] < start:
                    heappop(maxHeap)
                while minHeap[0][1] < start:
                    heappop(minHeap)
        return ans


# 2nd solution
# O(n) time | O(1) space 
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = left = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            while max(cnt) - min(cnt) > 2:
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                left += 1
            ans += right - left + 1
        return ans