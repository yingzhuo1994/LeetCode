# 1st solution
# O(nm^2) time | O(nm) space
# where n = len(factory) and m = len(robot)
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()
        n, m = len(factory), len(robot)
        @cache
        def f(i: int, j: int) -> int:
            if j == m: return 0
            if i == n - 1:
                if m - j > factory[i][1]: return inf
                return sum(abs(x - factory[i][0]) for x in robot[j:])
            res = f(i + 1, j)
            s, k = 0, 1
            while k <= factory[i][1] and j + k - 1 < m:
                s += abs(robot[j + k - 1] - factory[i][0])
                res = min(res, s + f(i + 1, j + k))
                k += 1
            return res
        return f(0, 0)