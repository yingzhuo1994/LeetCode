# 1st solution
class MyCalendar:
    def __init__(self):
        self.startTime = [0, float("inf")]
        self.endTime = [0, float("inf")]

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.startTime, start)
        if self.endTime[idx-1] <= start and end <= self.startTime[idx]:
            self.startTime.insert(idx, start)
            self.endTime.insert(idx, end)
            return True
        return False

# 2nd solution
# O(n*log(n)) time | O(n) space
from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        q1 = SortedList.bisect_right(self.calendar, start)
        q2 = SortedList.bisect_left(self.calendar, end)
        if q1 == q2 and q1 % 2 == 0:
            self.calendar.add(start)
            self.calendar.add(end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)