class CountIntervals:
    def __init__(self):
        self.intervals = [[float("inf"), float("inf")]]
        self.number = 0

    def add(self, left: int, right: int) -> None:
        idx = self.binarySearch(left)
        if idx > 0 and self.intervals[idx - 1][1] + 1 >= left:
            left = self.intervals[idx - 1][1] + 1
        if left > right:
            return

        i = idx
        while i < len(self.intervals):
            if self.intervals[i][1] <= right:
                self.number -= self.intervals[i][1] - self.intervals[i][0] + 1
            else:
                break
            i += 1
        self.number += right - left + 1
        self.intervals[idx:i] = [[left, right]]

        if idx > 0 and self.intervals[idx - 1][1] + 1 == left:
            self.intervals[idx - 1][1] = right
            self.intervals.pop(idx)
            idx -= 1

        if (
            idx + 1 < len(self.intervals)
            and self.intervals[idx + 1][0] - 1 <= self.intervals[idx][1]
        ):
            diff = max(0, self.intervals[idx][1] - self.intervals[idx + 1][0] + 1)
            self.number -= diff
            self.intervals[idx][1] = self.intervals[idx + 1][1]
            self.intervals.pop(idx + 1)

    def count(self) -> int:
        return self.number

    def binarySearch(self, val):
        left, right = 0, len(self.intervals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.intervals[mid][0] > val:
                right = mid - 1
            elif self.intervals[mid][0] < val:
                left = mid + 1
            else:
                return mid
        return left


# 2nd solution
class CountIntervals:
    __slots__ = "left", "right", "l", "r", "cnt"

    def __init__(self, l=1, r=10**9):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1:
            return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None:
            self.left = CountIntervals(self.l, mid)  # 动态开点
        if self.right is None:
            self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        if l <= mid:
            self.left.add(l, r)
        if mid < r:
            self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()