# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        stack = []
        lastTime = tasks[0][0]
        while len(ans) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= lastTime:
                heapq.heappush(stack, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
                i += 1
            if stack:
                t_diff, original_index = heapq.heappop(stack)
                lastTime += t_diff
                ans.append(original_index)
            elif i < len(tasks):
                lastTime = tasks[i][0]
        return ans