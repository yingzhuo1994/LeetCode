# 1st solution
# O(mn) time | O(1) space
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        dic4 = {i: 0 for i in range(5)}
        m, n = len(grid), len(grid[0])
        for i in range(m // 2):
            for j in range(n // 2):
                count = 0
                for x, y in [[i, j], [m - 1 - i, j], [i, n - 1 - j], [m - 1 - i, n - 1 - j]]:
                    if grid[x][y] == 1:
                        count += 1
                dic4[count] = dic4.get(count, 0) + 1

        dic2 = {i: 0 for i in range(3)}
        
        if m & 1:
            i = m // 2
            for j in range(n // 2):
                count = 0
                if grid[i][j] == 1:
                    count += 1
                if grid[i][n - 1 - j] == 1:
                    count += 1
                dic2[count] = dic2.get(count, 0) + 1
        if n & 1:
            j = n // 2
            for i in range(m // 2):
                count = 0
                if grid[i][j] == 1:
                    count += 1
                if grid[m - 1 - i][j] == 1:
                    count += 1
                dic2[count] = dic2.get(count, 0) + 1
        
        ones = 4 * (dic4[4] + dic4[3] + dic4[2]) + (dic2[1] + dic2[2]) * 2
        if m & 1 and n & 1:
            if grid[m // 2][n // 2] == 1:
                ones += 1
        ans = dic4[3] + dic4[2] * 2 + dic4[1] + dic2[1]

        r = ones % 4
        if r == 0:
            return ans
        else:
            if r == 2:
                if dic2[1] > 0:
                    return ans
                elif dic2[2] > 0:
                    return ans + 2
            if m & 1 and n & 1 and grid[m // 2][n // 2] == 1:
                if r == 1:
                    return ans + 1
                if r == 3:
                    if dic2[1] > 0:
                        return ans + 1
                    if dic2[2] > 0:
                        return ans + 3
            
            ans = sum(dic4[i] * i for i in range(5))
            ans += dic2[1] * 1 + dic2[2] * 2
            ans += m & 1 and n & 1 and grid[m // 2][n // 2] == 1
            return ans