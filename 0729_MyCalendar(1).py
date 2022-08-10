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

# 3rd solution
# O(n*log(n)) time | O(n) space
class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)