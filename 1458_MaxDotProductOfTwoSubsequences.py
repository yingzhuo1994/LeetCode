# 1st solution, TLE
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        minDic1 = {}
        maxDic1 = {}
        minDic2 = {}
        maxDic2 = {}
        def getMinMax(dicNum, l, r):
            if dicNum == 1:
                if (l, r) not in minDic1:
                    minDic1[(l, r)], maxDic1[(l, r)] = min(nums1[l:r+1]), max(nums1[l:r+1])
                return minDic1[(l, r)], maxDic1[(l, r)]
            else:
                if (l, r) not in minDic2:
                    minDic2[(l, r)], maxDic2[(l, r)] = min(nums2[l:r+1]), max(nums2[l:r+1])
                return minDic2[(l, r)], maxDic2[(l, r)]


        @cache
        def dp(l1, r1, l2, r2):
            a, b = getMinMax(1, l1, r1)
            c, d = getMinMax(2, l2, r2)
            
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