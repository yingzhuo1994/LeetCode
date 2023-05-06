# 1st solution, TLE
# O(n * log(n)) time | O(n) space
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
