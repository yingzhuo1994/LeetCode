# 1st solution
# O(n + m * log(m)) time | O(m) space
# where n = len(nums) and m = len(queries)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        events = []
        for l, r in queries:
            events.append([l, -1])
            events.append([r + 1, 1])
        events.sort()
        j = 0
        val = 0
        for i, num in enumerate(nums):
            while j < len(events) and events[j][0] <= i:
                val += events[j][1]
                j += 1
            if num + val > 0:
                return False
        return True

# 2nd solution
# (n + m) time | O(n) space
# where n = len(nums) and m = len(queries)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for l, r in queries:
            # 区间 [l,r] 中的数都加一
            diff[l] += 1
            diff[r + 1] -= 1

        for x, sum_d in zip(nums, accumulate(diff)):
            # 此时 sum_d 表示 x=nums[i] 要减掉多少
            if x > sum_d:  # x 无法变成 0
                return False
        return True