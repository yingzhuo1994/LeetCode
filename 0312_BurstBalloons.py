# 1st solution
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums, n = [1] + nums + [1], len(nums) + 2
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = max(nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        
        return dp[0][n-1]

# 2nd solution, not correct
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        array = [0] * (len(nums) + 2)
        n = 1
        for x in nums:
            if x > 0:
                array[n] = x
                n += 1
        array[0] = 1
        array[n] = 1
        print(array)
        n += 1
        
        memo = [[0] * n] * n
        return self.burst(memo, array, 0, n - 1)

    def burst(self, memo, nums, left, right):
        if left + 1 == right:
            return 0
        if memo[left][right] > 0:
            return memo[left][right]
        ans = 0
        for i in range(left + 1, right):
            ans = max(ans, nums[left] * nums[i] * nums[right] + self.burst(memo, nums, left, i) + self.burst(memo, nums, i, right))
        memo[left][right] = ans
        return ans   