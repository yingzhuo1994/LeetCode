# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)
        cnt = Counter()
        minHeap = []
        for i in range(n + 1):
            gap = startTime[i] - endTime[i - 1]
            cnt[gap] += 1
            heappush(minHeap, gap)
            if len(minHeap) > 3:
                heappop(minHeap)

        ans = 0
        for i in range(n):
            left = startTime[i] - endTime[i - 1]
            right = startTime[i + 1] - endTime[i]
            cnt[left] -= 1
            cnt[right] -= 1
            dur = endTime[i] - startTime[i]
            gap = left + right
            for num in minHeap:
                if num >= dur and cnt[num] > 0:
                    gap += dur
                    break
            ans = max(ans, gap)
            cnt[left] += 1
            cnt[right] += 1
        
        return ans