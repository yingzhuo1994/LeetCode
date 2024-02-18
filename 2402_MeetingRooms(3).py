# 1st solution
# O(m*log(m) + m*log(n)) time | O(n) space 
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        numbers = [0 for _ in range(n)]
        stack = []
        candidates = [i for i in range(n)]
        heapify(candidates)

        meetings.sort()
        for start, end in meetings:
            while stack and stack[0][0] <= start:
                t, idx = heappop(stack)
                heappush(candidates, idx)
            if not candidates:
                t, idx = heappop(stack)
                numbers[idx] += 1
                if t <= start:
                    heappush(stack, [end, idx])
                else:
                    heappush(stack, [t + end - start, idx])
            else:
                idx = heappop(candidates)
                numbers[idx] += 1
                heappush(stack, [end, idx])
                
        count, ans = -1, 0
        for idx, num in enumerate(numbers):
            if num > count:
                count = num
                ans = idx
        
        return ans
