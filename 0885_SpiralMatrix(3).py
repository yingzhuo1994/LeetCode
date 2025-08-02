# 1st solution
# O(max(m, n)^2) time | O(mn) space
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = rStart, cStart
        ans = []
        visited = set()
        idx = 0
        while len(ans) < rows * cols:
            dx, dy = dirs[idx]
            idx = (idx + 1) % 4
            dx1, dy1 = dirs[idx]
            while True:
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                    visited.add((i, j))
                i += dx
                j += dy
                x = i + dx1
                y = j + dy1
                if 0 <= x < rows and 0 <= y < cols:
                    if (x, y) not in visited:
                        break
                else:
                    break
        return ans


# 2nd solution
# O(max(m, n)^2) time | O(mn) space
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        dx, dy = 0, 1
        r = 0
        x, y = rStart, cStart
        while len(ans) < rows * cols:
            for _ in range(r // 2 + 1):
                if 0 <= x < rows and 0 <= y < cols:
                    ans.append([x, y])
                x += dx
                y += dy
            dx, dy = dy, -dx
            r += 1
        return ans