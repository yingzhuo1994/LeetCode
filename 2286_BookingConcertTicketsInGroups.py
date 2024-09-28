# 1st solution
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.minTree = [0] * (4 * n)
        self.sumTree = [0] * (4 * n)

    def modify(self, i: int, l: int, r: int, index: int, val: int):
        if l == r:
            self.minTree[i] = val
            self.sumTree[i] = val
            return
        mid = (l + r) // 2
        if index <= mid:
            self.modify(i * 2, l, mid, index, val)
        else:
            self.modify(i * 2 + 1, mid + 1, r, index, val)
        self.minTree[i] = min(self.minTree[i * 2], self.minTree[i * 2 + 1])
        self.sumTree[i] = self.sumTree[i * 2] + self.sumTree[i * 2 + 1]

    def queryMinRow(self, i: int, l: int, r: int, val: int) -> int:
        if l == r:
            return l if self.minTree[i] <= val else self.n
        mid = (l + r) // 2
        if self.minTree[i * 2] <= val:
            return self.queryMinRow(i * 2, l, mid, val)
        else:
            return self.queryMinRow(i * 2 + 1, mid + 1, r, val)

    def querySum(self, i: int, l: int, r: int, l2: int, r2: int) -> int:
        if l2 <= l and r <= r2:
            return self.sumTree[i]
        mid = (l + r) // 2
        totalSum = 0
        if mid >= l2:
            totalSum += self.querySum(i * 2, l, mid, l2, r2)
        if mid + 1 <= r2:
            totalSum += self.querySum(i * 2 + 1, mid + 1, r, l2, r2)
        return totalSum

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.queryMinRow(1, 0, self.n - 1, self.m - k)
        if i > maxRow:
            return []
        used = self.querySum(1, 0, self.n - 1, i, i)
        self.modify(1, 0, self.n - 1, i, used + k)
        return [i, used]

    def scatter(self, k: int, maxRow: int) -> bool:
        usedTotal = self.querySum(1, 0, self.n - 1, 0, maxRow)
        if (maxRow + 1) * self.m - usedTotal < k:
            return False
        i = self.queryMinRow(1, 0, self.n - 1, self.m - 1)
        while True:
            used = self.querySum(1, 0, self.n - 1, i, i)
            if self.m - used >= k:
                self.modify(1, 0, self.n - 1, i, used + k)
                break
            k -= self.m - used
            self.modify(1, 0, self.n - 1, i, self.m)
            i += 1
        return True


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)