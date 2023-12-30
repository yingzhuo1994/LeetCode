# 1st solution
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
            x = datetime.datetime(year, month, day)
            return x.strftime("%A")

# 2nd solution, Zeller's congruence
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            year -= 1
            month += 12
        
        b = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        c = year // 100
        y = year - 100 * c
        w = c // 4 - 2 * c + y + y // 4 + 26 * (month + 1) // 10 + day - 1
        w = (w % 7 + 7) % 7
        return b[w]