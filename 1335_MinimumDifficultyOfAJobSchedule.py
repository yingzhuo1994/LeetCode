# 1st solution
# O(kn^2) time | O(kn) space
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
       
        @cache
        def dfs(start, k):
            if k == 0:
                return max(jobDifficulty[start:])
            elif n - start == k + 1:
                return sum(jobDifficulty[start:])
            elif n - start < k + 1:
                return float("inf")
            
            diff = -1
            ans = float("inf")
            for i in range(start, n - k):
                diff = max(diff, jobDifficulty[i])
                ans = min(ans, dfs(i+1, k-1) + diff)
            
            return ans
        
        ans = dfs(0, d - 1)
        return ans if ans != float("inf") else -1

# 2nd solution
# O(kn^2) time | O(kn) space
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float("inf") for _ in range(n)] for _ in range(d)]
        for k in range(d):
            for i in range(n - k):
                if k == 0:
                    dp[k][i] = max(jobDifficulty[i:])
                    continue

                diff = -1
                ans = float("inf")
                for j in range(i, n - k):
                    diff = max(diff, jobDifficulty[j])
                    ans = min(ans, dp[k-1][j+1] + diff)
                dp[k][i] = ans

        return dp[d-1][0]

# 3rd solution, Top-down DP
# O(dn^2) time | O(dn) space
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == 0:  # 只有一天，必须完成所有工作
                return max(a[:j + 1])
            res, mx = inf, 0
            for k in range(j, i - 1, -1):
                mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                res = min(res, dfs(i - 1, k - 1) + mx)
            return res

        return dfs(d - 1, n - 1)

# 4th solution, Bottom-up DP
# O(dn^2) time | O(dn) space
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        f = [[inf] * n for _ in range(d)]
        f[0] = list(accumulate(a, max))
        for i in range(1, d):
            for j in range(i, n):
                mx = 0
                for k in range(j, i - 1, -1):
                    mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                    f[i][j] = min(f[i][j], f[i - 1][k - 1] + mx)
        return f[-1][-1]

# 5th solution, Bottom-up DP, space optimized
# O(dn^2) time | O(n) space
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        f = list(accumulate(a, max))
        for i in range(1, d):
            for j in range(n - 1, i - 1, -1):
                f[j] = inf
                mx = 0
                for k in range(j, i - 1, -1):
                    mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                    f[j] = min(f[j], f[k - 1] + mx)
        
        return f[-1]

# 6th solution, Monotonic Stack
# O(dn) time | O(dn) space
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        f = [[inf] * n for _ in range(d)]
        f[0] = list(accumulate(a, max))
        for i in range(1, d):
            st = []  # (下标 j，从 f[i-1][left[j]] 到 f[i-1][j-1] 的最小值)
            for j in range(i, n):
                mn = f[i - 1][j - 1]  # 只有 a[j] 一项工作
                while st and a[st[-1][0]] <= a[j]:  # 向左一直计算到 left[j]
                    mn = min(mn, st.pop()[1])
                f[i][j] = mn + a[j]  # 从 a[left[j]+1] 到 a[j] 的最大值是 a[j]
                if st:  # 如果这一段包含 <=left[j] 的工作，那么这一段的最大值必然不是 a[j]
                    f[i][j] = min(f[i][j], f[i][st[-1][0]])  # 答案和 f[i][left[j]] 是一样的
                st.append((j, mn))  # 注意这里保存的不是 f[i][j]
        return f[-1][-1]