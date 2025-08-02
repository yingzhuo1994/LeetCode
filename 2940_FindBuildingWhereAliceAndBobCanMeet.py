# 1st solution
# O(n + q * log(q)) time | O(n + q) space
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        qs = [[] for _ in heights]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a  # 保证 a <= b
            if a == b or heights[a] < heights[b]:
                ans[i] = b  # a 直接跳到 b
            else:
                qs[b].append((heights[a], i))  # 离线询问

        h = []
        for i, x in enumerate(heights):
            while h and h[0][0] < x:
                # 堆顶的 heights[a] 可以跳到 heights[i]
                ans[heappop(h)[1]] = i
            for q in qs[i]:
                heappush(h, q)  # 后面再回答
        return ans