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


# 2nd solution
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (2 << n.bit_length())  # 相比 4n 空间更小
        self.sum = [0] * (2 << n.bit_length())

    # 线段树：把下标 i 上的元素值增加 val
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 线段树：返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = self.query_sum(o * 2, l, m, L, R)
        if R > m:
            res += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return res

    # 线段树：返回区间 [0,R] 中 <= val 的最靠左的位置，不存在时返回 -1
    def find_first(self, o: int, l: int, r: int, R: int, val: int) -> int:
        if self.min[o] > val:
            return -1  # 整个区间的元素值都大于 val
        if l == r:
            return l
        m = (l + r) // 2
        if self.min[o * 2] <= val:
            return self.find_first(o * 2, l, m, R, val)
        if R > m:
            return self.find_first(o * 2 + 1, m + 1, r, R, val)
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        # 找第一个能倒入 k 升水的水桶
        r = self.find_first(1, 0, self.n - 1, maxRow, self.m - k)
        if r < 0:  # 没有这样的水桶
            return []
        c = self.query_sum(1, 0, self.n - 1, r, r)
        self.update(1, 0, self.n - 1, r, k)  # 倒水
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        # [0,maxRow] 的接水量之和
        s = self.query_sum(1, 0, self.n - 1, 0, maxRow)
        if s > self.m * (maxRow + 1) - k:
            return False  # 水桶已经装了太多的水
        # 从第一个没有装满的水桶开始
        i = self.find_first(1, 0, self.n - 1, maxRow, self.m - 1)
        while k:
            left = min(self.m - self.query_sum(1, 0, self.n - 1, i, i), k)
            self.update(1, 0, self.n - 1, i, left)  # 倒水
            k -= left
            i += 1
        return True
    

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)