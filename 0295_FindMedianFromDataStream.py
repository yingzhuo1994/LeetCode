class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = collections.deque([])
        self.length = 0
        

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.array.append(num)
        else:
            a, b = 0, self.length - 1
            m = (a + b) // 2
            while a < b:
                if num < self.array[m]:
                    b = m - 1
                elif num > self.array[m]:
                    a = m + 1
                else:
                    a = m
                    break
                m = (a + b) // 2
            if num <= self.array[a]:
                self.array.insert(a, num)
            else:
                self.array.insert(b + 1, num)
        self.length += 1

    def findMedian(self) -> float:
        n = self.length
        if n > 0:
            if n & 1:
                return float(self.array[n // 2])
            else:
                return float(self.array[n // 2] + self.array[n // 2 - 1]) / 2.0


# 2nd solution
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    # O(log n) time
    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    # O(1) time
    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0