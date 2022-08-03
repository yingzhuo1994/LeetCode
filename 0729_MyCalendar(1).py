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
    
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)