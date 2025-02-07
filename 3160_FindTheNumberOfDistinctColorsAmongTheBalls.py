# 1st solution
# O(n) time | O(n) space
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        balls = {}
        ans = []
        for x, y in queries:
            if balls.get(x, 0) > 0:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    del colors[balls[x]]
            balls[x] = y
            if y not in colors:
                colors[y] = 0
            colors[y] += 1
            ans.append(len(colors))
        return ans