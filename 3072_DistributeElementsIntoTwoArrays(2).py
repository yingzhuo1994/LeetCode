# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1 =[nums[0]]
        nums2 = [nums[1]]
        lst1 = [nums[0]]
        lst2 = [nums[1]]
        for i in range(2, len(nums)):
            a = len(nums1) - bisect.bisect_right(nums1, nums[i])
            b = len(nums2) - bisect.bisect_right(nums2, nums[i])
            if a > b:
                nums1.insert(len(nums1) - a, nums[i])
                lst1.append(nums[i])
            elif a < b:
                nums2.insert(len(nums2) - b, nums[i])
                lst2.append(nums[i])
            else:
                if len(nums1) <= len(nums2):
                    nums1.insert(len(nums1) - a, nums[i])
                    lst1.append(nums[i])
                else:
                    nums2.insert(len(nums2) - b, nums[i])
                    lst2.append(nums[i])
        return lst1 + lst2


# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t1 = Fenwick(m + 1)
        t2 = Fenwick(m + 1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            gc1 = len(a) - t1.pre(v)  # greaterCount(a, v)
            gc2 = len(b) - t2.pre(v)  # greaterCount(b, v)
            if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
                a.append(x)
                t1.add(v)
            else:
                b.append(x)
                t2.add(v)
        return a + b
    

class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 1
    def add(self, i: int) -> None:
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


# 3rd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t = Fenwick(m + 1)
        t.add(m - bisect_left(sorted_nums, nums[0]), 1)
        t.add(m - bisect_left(sorted_nums, nums[1]), -1)
        for x in nums[2:]:
            v = m - bisect_left(sorted_nums, x)
            d = t.pre(v - 1)  # 转换成 < v 的元素个数之差
            if d > 0 or d == 0 and len(a) <= len(b):
                a.append(x)
                t.add(v, 1)
            else:
                b.append(x)
                t.add(v, -1)
        return a + b

class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 v
    def add(self, i: int, v: int) -> None:
        while i < len(self.tree):
            self.tree[i] += v
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res