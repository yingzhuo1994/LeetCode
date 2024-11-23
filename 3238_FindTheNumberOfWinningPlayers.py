# 1st solution
# O(n + k) time | O(n + k) space
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        scores = [{} for _ in range(n)]
        for x, y in pick:
            scores[x][y] = scores[x].get(y, 0) + 1
        count = 0
        for i, score in enumerate(scores):
            if score and max(score.values()) > i:
                count += 1
        return count
