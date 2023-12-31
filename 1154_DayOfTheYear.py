# 1st solution
# O(1) time | O(1) space
class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        ans = 0
        for i in range(month - 1):
            ans += months[i]
        ans += day
        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            ans += 1
        return ans

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
        return d + sum(days[:m-1])