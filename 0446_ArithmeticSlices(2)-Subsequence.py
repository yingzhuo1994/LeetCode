class Solution:
    # 1st solution
    # O(2^n) time | O(n) space
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def dfs(dep, A, cur):
            if dep == n:
                if len(cur) < 3:
                    return
                diff = cur[1] - cur[0]
                for i in range(1, len(cur)):              
                    if cur[i] - cur[i - 1] != diff:
                        return
                self.ans += 1
                return
            dfs(dep + 1, A, cur)
            cur.append(A[dep])
            dfs(dep + 1, A, cur)
            cur.remove(A[dep])

        n = len(nums)
        self.ans = 0
        cur = []
        dfs(0, nums, cur)
        return self.ans   

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total, n = 0, len(nums)
        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)      
            total += sum(dp[i].values())
          
        return total - (n - 1) * n // 2  
