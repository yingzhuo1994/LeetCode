# 1st solution
# O(2^n) time | O(n) space
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        def dfs(idx, lst):
            if idx == len(nums):
                return len(lst) > 0
            count = 0
            count += dfs(idx + 1, lst)
            i = bisect.bisect_left(lst, nums[idx] - k)
            if i < len(lst) and lst[i] == nums[idx] - k:
                return count
            count += dfs(idx + 1, lst + [nums[idx]])
            return count
        return dfs(0, [])


# 2nd solution
# O(n * log(n) + k) time | O(n + k) space
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = [Counter() for i in range(k)]
        for num in nums:
            count[num % k][num] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for num in sorted(count[i]):
                v = pow(2, count[i][num])
                if prev + k == num:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = num
            res *= dp0 + dp1
        return res - 1

# 3rd solution
# O(n * log(n) + k) time | O(n + k) space
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            groups[x % k][x] += 1
        ans = 1
        for cnt in groups.values():
            g = sorted(cnt.items())
            m = len(g)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << g[0][1]
            for i in range(1, m):
                if g[i][0] - g[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << g[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << g[i][1]
            ans *= f[m]
        return ans - 1  # -1 去掉空集