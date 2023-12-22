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