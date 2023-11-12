# 1st solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 返回能否在初始位置停留 t 分钟，并安全到达安全屋
        def check(t: int) -> bool:
            f = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 1]
            on_fire = set(f)  # 标记着火的位置
            def spread_fire():
                # 火的 BFS
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in on_fire:
                            on_fire.add((x, y))  # 标记着火的位置
                            f.append((x, y))
            while t and f:  # 如果火无法扩散就提前退出
                spread_fire()  # 火扩散
                t -= 1
            if (0, 0) in on_fire:
                return False  # 起点着火，寄

            # 人的 BFS
            q = [(0, 0)]
            vis = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) in on_fire: continue  # 人走到这个位置后，火也扩散到了这个位置
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in on_fire and (x, y) not in vis:
                            if x == m - 1 and y == n - 1:
                                return True  # 我们安全了…暂时。
                            vis.add((x, y))  # 避免反复访问同一个位置
                            q.append((x, y))
                spread_fire()  # 火扩散
            return False  # 人被火烧到，或者没有可以到达安全屋的路

        # 这里我用开区间二分（其它写法也可以）
        left = -1
        right = m * n + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left if left < m * n else 10 ** 9

# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 返回三个数，分别表示到达安全屋/安全屋左边/安全屋上边的最短时间
        def bfs(q: List[Tuple[int, int]]) -> (int, int, int):
            time = [[-1] * n for _ in range(m)]  # -1 表示未访问
            for i, j in q:
                time[i][j] = 0
            t = 1
            while q:  # 每次循环向外扩展一圈
                tmp = q
                q = []
                for i, j in tmp:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and time[x][y] < 0:
                            time[x][y] = t
                            q.append((x, y))
                t += 1
            return time[-1][-1], time[-1][-2], time[-2][-1]

        man_to_house_time, m1, m2 = bfs([(0, 0)])
        if man_to_house_time < 0:  # 人无法到安全屋
            return -1

        fire_pos = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 1]
        fire_to_house_time, f1, f2 = bfs(fire_pos)
        if fire_to_house_time < 0:  # 火无法到安全屋
            return 10 ** 9

        d = fire_to_house_time - man_to_house_time
        if d < 0:  # 火比人先到安全屋
            return -1

        if m1 != -1 and m1 + d < f1 or \
           m2 != -1 and m2 + d < f2:  # 安全屋左边或上边的其中一个格子人比火先到
            return d  # 图中第一种情况
        return d - 1  # 图中第二种情况

