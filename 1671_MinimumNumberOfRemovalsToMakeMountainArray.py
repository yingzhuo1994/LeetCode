# 1st solution, TLE
# O(n^3) time | O(n) space
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def leftLongestStack(peakIdx):
            lengthDic = {peakIdx: 0}
            for i in reversed(range(peakIdx)):
                lengthDic[i] = 0
                for j in range(i + 1, peakIdx + 1):
                    if nums[i] < nums[j]:
                        lengthDic[i] = max(lengthDic[i], lengthDic[j] + 1)

            return max(lengthDic.values())
        
        def rightLongestStack(peakIdx):
            lengthDic = {peakIdx: 0}
            for i in range(peakIdx + 1, n):
                lengthDic[i] = 0
                for j in range(peakIdx, i):
                    if nums[i] < nums[j]:
                        lengthDic[i] = max(lengthDic[i], lengthDic[j] + 1)

            return max(lengthDic.values())
        
        n = len(nums)
        ans = n
        for i in range(1, n - 1):
            leftLength = leftLongestStack(i)
            if leftLength <= 0:
                continue
            rightLength = rightLongestStack(i)
            if rightLength <= 0:
                continue
            length = leftLength + rightLength + 1
            ans = min(ans, n - length)
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        g = []
        for i in range(n - 1, 0, -1):
            x = nums[i]
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            suf[i] = j + 1  # 从 nums[i] 开始的最长严格递减子序列的长度

        mx = 0  # 最长山形子序列的长度
        g = []
        for i, x in enumerate(nums):
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            pre = j + 1  # 在 nums[i] 结束的最长严格递增子序列的长度
            if pre >= 2 and suf[i] >= 2:
                mx = max(mx, pre + suf[i] - 1)  # 减去重复的 nums[i]
        return n - mx