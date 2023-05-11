# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        set2 = set(nums2)
        
        @cache
        def dfs(topIdx, startIdx):
            if topIdx == len(nums1) or startIdx == len(nums2):
                return 0
            topNum = nums1[topIdx]
            if topNum not in set2:
                return dfs(topIdx + 1, startIdx)
            ans = 0
            for j in range(startIdx, len(nums2)):
                if nums2[j] == topNum:
                    ans = max(ans, dfs(topIdx + 1, j + 1) + 1)
            ans = max(ans, dfs(topIdx + 1, startIdx))

            return ans

        return dfs(0, 0)

# 2nd solution, DP
# O(mn) time | O(mn) space
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(nums1), len(nums2)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (nums1[i] == nums2[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]