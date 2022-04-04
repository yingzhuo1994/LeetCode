# 1st solution
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + num
        sortedKeys = sorted(dic.keys())
        dp = {}
        for k in range(sortedKeys[0], sortedKeys[-1] + 1):
            if k - 2 not in dp:
                dp[k - 2] = 0
            if k - 1 not in dp:
                dp[k - 1] = 0
            dp[k] = dp[k - 1]
            dp[k] = max(dp[k], dp[k-2] + dic.get(k, 0))
        return dp[sortedKeys[-1]]

# 2nd solution
# O(n + k*log(k)) time | O(k) space
# where n is the number of nums, and k is the unique number of nums
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pointsDic = {}
        for num in nums:
            pointsDic[num] = pointsDic.get(num, 0) + num
        sortedKeys = sorted(pointsDic.keys())
        frontTwo = 0
        frontOne = 0
        ans = 0
        for k in sortedKeys:
            frontTwo = frontOne if k - 1 in pointsDic else ans
            frontOne = ans
            ans = max(frontOne, frontTwo + pointsDic[k])
        return ans