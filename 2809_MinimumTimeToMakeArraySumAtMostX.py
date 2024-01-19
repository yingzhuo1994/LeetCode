# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        n = len(pairs)
        f = [0] * (n + 1)
        for i, (a, b) in enumerate(pairs):
            for j in range(i + 1, 0, -1):
                f[j] = max(f[j], f[j - 1] + a + b * j)

        s1 = sum(nums1)
        s2 = sum(nums2)
        for t, v in enumerate(f):
            if s1 + s2 * t - v <= x:
                return t
        
        return -1

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        if sum(nums1) <= x:
            return 0
        
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        n = len(pairs)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i, (a, b) in enumerate(pairs):
            for j in range(1, i + 2):
                dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + a + b * j)

        s1 = sum(nums1)
        s2 = sum(nums2)
        for t, v in enumerate(dp[n]):
            if s1 + s2 * t - v <= x:
                return t
        
        return -1