# 1st solution, TLE
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        @cache
        def dp(l1, r1, l2, r2):
            a, b = min(nums1[l1:r1+1]), max(nums1[l1:r1+1])
            c, d = min(nums2[l2:r2+1]), max(nums2[l2:r2+1])
            
            return max(a * c, a * d, b * c, b * d)
        
        @cache
        def dfs(m, n, k):
            if k == 1:
                ans = dp(0, m -1, 0, n - 1)
            else:
                ans = float("-inf")
                for i in range(k - 1, m):
                    for j in range(k - 1, n):
                        value = dfs(i, j, k - 1) + dp(i, m - 1, j, n - 1)
                        ans = max(ans, value)
            # print([m, n, k], "value: ", ans)
            return ans

        dp(0, n1-1, 0, n2-1)

        length = min(n1, n2)
        ans = float("-inf")
        for k in range(1, length + 1):
            value = dfs(n1, n2, k)
            # print([n1, n2, k], "ans: ", value)
            ans = max(ans, value)

        return ans