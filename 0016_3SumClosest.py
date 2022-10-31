# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = float("inf")
        for i in range(len(nums)):
            curTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum < curTarget:
                    left += 1
                elif curSum > curTarget:
                    right -= 1
                else:
                    return target
                if abs(curSum - curTarget) < abs(ans - target):
                    ans = curSum + nums[i]
        return ans

# 2nd solution
# O(max(n^(max(k-1, 1))), n*log(n)) time | O(kn) space
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        smallSum = sum(nums[:k])
        if smallSum >= target:
            return smallSum

        # target too big
        largeSum = sum(nums[-k:])
        if largeSum <= target:
            return largeSum
        
        if k == 1:
            idx = bisect.bisect_left(nums, target)
            if idx == N:
                return nums[-1]
            elif idx == 0:
                return nums[0]
            
            if abs(nums[idx - 1] - target) <= abs(nums[idx] - target):
                return nums[idx - 1]
            else:
                return nums[idx]
        
        if k == 2:
            closest = float("inf")
            left, right = 0, len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum < target:
                    left += 1
                elif curSum > target:
                    right -= 1
                else:
                    return target
                if abs(curSum - target) < abs(closest - target):
                    closest = curSum
            return closest
            
        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            curSum = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if curSum == target:
                return target
            if abs(target - curSum) < abs(target - closest):
                if curSum == target:
                    return target
                else:
                    closest = curSum

        return closest