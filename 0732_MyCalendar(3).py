# 1st solution
# O(n*log(n)) time | O(n) space
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

# 2nd solution, Segment Tree
# O(n*log(C)) time | O(n*log(C)) space
# where n is the number of events booked and C is the largest time
from collections import Counter
class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def update(self, start: int, end: int, left: int = 0, right: int = 10**9, idx: int = 1) -> None:
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (left + right)//2
            self.update(start, end, left, mid, idx*2)
            self.update(start, end, mid+1, right, idx*2 + 1)
            self.vals[idx] = self.lazy[idx] + \
                max(self.vals[2*idx], self.vals[2*idx+1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end-1)
        return self.vals[1]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)