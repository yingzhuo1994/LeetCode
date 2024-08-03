# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dic = {}
        for (x, y), ch in zip(points, s):
            d = max(abs(x), abs(y))
            if d not in dic:
                dic[d] = []
            dic[d].append(ch)
        edges = sorted(list(dic.keys()))
        ans = 0
        labels = set()
        for edge in edges:
            edge_set = set(dic[edge])
            if len(dic[edge]) != len(edge_set):
                return ans
            common = labels & edge_set
            if len(common) != 0:
                return ans
            ans += len(edge_set)
            labels |= edge_set
        return ans