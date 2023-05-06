# 1st solution, TLE
# O(n * log(n)) time | O(n) space
import bisect


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        n = len(nums)
        nums.sort()
        # print(nums)
        for i in reversed(range(n)):
            maxV = nums[i]
            # print(f"idx: {i}")
            left = bisect.bisect_right(nums, target - maxV, hi=i)
            right = i - left
            # print(i, nums[i], left, right)
            count = (pow(2, left) - 1) * pow(2, right) % MOD
            if 2 * maxV <= target:
                count += 1
            # print(count)
                
            ans += count
            ans %= MOD
        
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        MOD = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, MOD)
                l += 1
        return res % MOD