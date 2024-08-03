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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_d = defaultdict(lambda: inf)
        min2 = inf
        for (x, y), c in zip(points, s):
            d = max(abs(x), abs(y))
            if d < min_d[c]:
                # d 是目前最小的，那么 min_d[c] 是次小的
                min2 = min(min2, min_d[c])
                min_d[c] = d
            else:
                # d 可能是次小的
                min2 = min(min2, d)
        return sum(d < min2 for d in min_d.values())