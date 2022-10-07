# 1st solution
import sortedcontainers
class MyCalendarThree:

    def __init__(self):
        self.diff = sortedcontainers.SortedDict({0: 0})
        self.maxBooking = 0

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        
        count = list(accumulate(self.diff.values()))

        return max(count)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)