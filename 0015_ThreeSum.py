class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1st solution
        # O(n^2) time | O(n) space
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
