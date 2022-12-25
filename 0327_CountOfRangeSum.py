# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        array = [0]
        for i in range(n):
            array.append(array[-1] + nums[i])
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                curSum = array[i] - array[j - 1]
                if lower <= curSum <= upper:
                    ans += 1
        return ans

# 2nd solution, mergesort
# O(n * log(n)) time | O(n) space
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        array = [0]
        for num in nums:
            array.append(array[-1] + num)
        def mergesort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = mergesort(lo, mid) + mergesort(mid, hi)
            i = j = mid
            for left in array[lo:mid]:
                while i < hi and array[i] - left <  lower: i += 1
                while j < hi and array[j] - left <= upper: j += 1
                count += j - i
            array[lo:hi] = sorted(array[lo:hi])
            return count
        return mergesort(0, len(array))

# 3rd solution, mergesort
# O(n * log(n)) time | O(n) space
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        array = [0]
        for num in nums:
            array.append(array[-1] + num)
        def mergesort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = mergesort(lo, mid) + mergesort(mid, hi)
            i = j = mid
            for val in array[lo:mid]:
                i = bisect.bisect_left(array, val + lower, lo=mid, hi=hi)
                j = bisect.bisect_right(array, val + upper, lo=mid, hi=hi)
                count += j - i
            lst = []
            i, j = lo, mid
            while i < mid and j < hi:
                if array[i] <= array[j]:
                    lst.append(array[i])
                    i += 1
                else:
                    lst.append(array[j])
                    j += 1
            lst.extend(array[i:mid] or array[j:hi])
            array[lo:hi] = lst
            return count
        return mergesort(0, len(array))