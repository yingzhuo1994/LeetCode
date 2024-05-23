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
        for a in nums:
            count[a % k][a] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for a in sorted(count[i]):
                v = pow(2, count[i][a])
                if prev + k == a:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = a
            res *= dp0 + dp1
        return res - 1