# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        MOD = 10**9 + 7
        minStack = []
        for i, num in enumerate(nums):
            heappush(minStack, [num, i])
        target = max(nums)
        while k > 0:
            k -= 1
            num, i = heappop(minStack)
            nums[i] = num * multiplier
            heappush(minStack, [nums[i], i])
            if nums[i] > target:
                break
            target = max(target, nums[i])
        q, r = divmod(k, len(nums))
        if q > 0:
            m = pow(multiplier, q, MOD)
        else:
            m = 1
        for _ in range(r):
            num, i = heappop(minStack)
            nums[i] = num * multiplier
            heappush(minStack, [nums[i], i])          
        for i, num in enumerate(nums):
            nums[i] = nums[i] * m % MOD
        return nums