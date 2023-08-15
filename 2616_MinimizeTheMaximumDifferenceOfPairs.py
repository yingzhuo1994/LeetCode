class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        A = nums
        n = len(A)
        A.sort()
        l, r = 0, A[n - 1] - A[0]
        while l < r:
            mid = (l + r) // 2
            if self.helper(A, mid, p) >= p:
                r = mid
            else:
                l = mid + 1
        return l
    
    def helper(self, A: List[int], diff: int, p: int) -> int:
        i, count = 1, 0
        while i < len(A):
            if A[i] - A[i - 1] <= diff:
                i += 1
                count += 1
            i += 1
        return count