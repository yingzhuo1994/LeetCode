# 1st solution
# O(1) time | O(1) space
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        dic = {}
        mask = "".join(map(str, cells))
        dic[mask] = 0
        days = [cells]
        for day in range(1, n + 1):
            new = cells[:]
            new[0] = 0
            new[-1] = 0
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1] or cells[i - 1] == cells[i + 1]:
                    new[i] = 1
                else:
                    new[i] = 0
            cells = new
            days.append(new)
            mask = "".join(map(str, cells))
            if mask in dic:
                cycle = day - dic[mask]
                r = (n - day) % cycle + 1
                return days[dic[mask] + r - 1]
            else:
                dic[mask] = day
        return cells