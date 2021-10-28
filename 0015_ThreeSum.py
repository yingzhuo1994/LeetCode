class Solution:
    # 1st solution
    # O(n^2) time | O(n) space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        lst = []
        for i in range(n - 2):
            p1 = i + 1
            p2 = n - 1
            curGoal = 0 - nums[i]
            while p1 < p2:
                curSum = nums[p1] + nums[p2]
                if curSum > curGoal:
                    p2 -= 1
                elif curSum < curGoal:
                    p1 += 1
                else:
                    curLst = [nums[i], nums[p1], nums[p2]]
                    if curLst not in lst:
                        lst.append(curLst)
                    p1 += 1
                    p2 -= 1
        return lst

    # 2nd solution
    # O(n^2) time | O(n) space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            curTarget = target - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > curTarget:
                    right -= 1
                elif nums[left] + nums[right] < curTarget:
                    left += 1
                else:
                    curLst = [nums[i], nums[left], nums[right]]
                    if not result or curLst != result[-1]:
                        result.append(curLst)
                    left += 1
                    right -= 1
        return result