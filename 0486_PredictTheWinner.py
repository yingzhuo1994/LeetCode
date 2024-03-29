# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n & 1:
            lastPlayer = 1
            dp = {(i, i): [num, 0] for i, num in enumerate(nums)}
        else:
            lastPlayer = -1
            dp = {(i, i): [0, num] for i, num in enumerate(nums)}
        
        player = lastPlayer * -1
        for i in reversed(range(1, n)):
            for j in range(i):
                start, end = j, j + n - i
                leftScores = dp[(start, end - 1)]
                leftDiff = leftScores[0] - leftScores[1] + player * nums[end]
                rightScores = dp[(start + 1, end)]
                rightDiff = rightScores[0] - rightScores[1] + player * nums[start]
                if leftDiff * player >= rightDiff * player:
                    if player > 0:
                        dp[(start, end)] = [leftScores[0] + nums[end], leftScores[1]]
                    else:
                        dp[(start, end)] = [leftScores[0], leftScores[1] + nums[end]]
                else:
                    if player > 0:
                        dp[(start, end)] = [rightScores[0] + nums[start], rightScores[1]]
                    else:
                        dp[(start, end)] = [rightScores[0], rightScores[1] + nums[start]]
            player = player * -1
        return dp[(0, n - 1)][0] >= dp[(0, n - 1)][1]

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp[i][j] the person's effective score when pick, facing nums[i..j]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for s in range(len(nums)):
            for i in range(len(nums)-s):
                j = i + s
                if i == j:
                    dp[i][i] = nums[i]
                else:
                    dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])
        return dp[0][-1] >= 0

# 3rd solution
# O(n^2) time | O(n) space
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for s in range(1, n):
            for i in range(n - s):
                j = i + s
                left = -dp[i] + nums[j]
                right = -dp[i+1] + nums[i]
                dp[i] = max(left, right)

        return dp[0] >= 0