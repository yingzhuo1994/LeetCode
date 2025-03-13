# 1st solution, TLE
# O(nq) time | O(1) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        zeros = sum(num == 0 for num in nums)
        n = len(nums)
        if zeros == n:
            return 0
        for i, query in enumerate(queries, 1):
            l, r, val = query
            for j in range(l, r + 1):
                if nums[j] > 0:
                    nums[j] = max(0, nums[j] - val)
                    if nums[j] == 0:
                        zeros += 1
            if zeros == n:
                return i
        return -1


# 2nd solution
# O((n + q) * log(q)) time | O(n) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # 3355. 零数组变换 I
        def check(k: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for l, r, val in queries[:k]:  # 前 k 个询问
                diff[l] += val
                diff[r + 1] -= val

            for x, sum_d in zip(nums, accumulate(diff)):
                if x > sum_d:
                    return False
            return True

        q = len(queries)
        left, right = -1, q + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if right <= q else -1


# 3rd solution
# O(n + q * log(n)) time | O(n) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = 2 << n.bit_length()
        mx = [0] * m
        todo = [0] * m

        def do(o: int, v: int) -> None:
            mx[o] -= v
            todo[o] += v

        def spread(o: int) -> None:
            if todo[o] != 0:
                do(o * 2, todo[o])
                do(o * 2 + 1, todo[o])
                todo[o] = 0

        def maintain(o: int) -> None:
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        def build(o: int, l: int, r: int) -> None:
            if l == r:
                mx[o] = nums[l]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)

        def update(o: int, l: int, r: int, ql: int, qr: int, v: int) -> None:
            if ql <= l and r <= qr:
                do(o, v)
                return
            spread(o)
            m = (l + r) // 2
            if ql <= m:
                update(o * 2, l, m, ql, qr, v)
            if m < qr:
                update(o * 2 + 1, m + 1, r, ql, qr, v)
            maintain(o)

        build(1, 0, n - 1)
        if mx[1] <= 0:
            return 0

        for i, (ql, qr, v) in enumerate(queries):
            update(1, 0, n - 1, ql, qr, v)
            if mx[1] <= 0:
                return i + 1
        return -1