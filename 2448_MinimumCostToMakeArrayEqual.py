# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calculate_cost(target):
            left = [0, 0]
            right = [0, 0]
            for i in range(len(nums)):
                if nums[i] < target:
                    left[0] += (target - nums[i]) * cost[i]
                    left[1] += cost[i]
                elif nums[i] > target:
                    right[0] += (nums[i] - target) * cost[i]
                    right[1] += cost[i]
            
            return left, right

        start = min(nums)
        end = max(nums)

        ans = float("inf")
        while start <= end:
            mid = start + (end - start) // 2
            left, right = calculate_cost(mid)
            totalCost = left[0] + right[0]
            ans = min(ans, totalCost)
            if left[1] > right[1]:
                end = mid - 1
            elif left[1] < right[1]:
                start = mid + 1
            else:
                break
        return ans

# 2nd solution
# O(n * log(n)) time | O(1) space
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def f(x):
            return sum(abs(a - x) * c for a,c in zip(nums, cost))

        l, r = min(nums), max(nums)
        res = f(l)
        while l < r:
            x = (l + r) // 2
            y1, y2 = f(x), f(x + 1)
            res = min(y1, y2)
            if y1 < y2:
                r = x
            else:
                l = x + 1
        return res