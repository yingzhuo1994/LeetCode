# 1st solution
# O(n) time | O(n) space
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countFunc(start, end):
            if start > end:
                return 0
            indices = [i for i in range(start, end + 1) if nums[i] >= left]
            if len(indices) == 0:
                return 0
            count = 0
            j = 0
            for i in range(start, end + 1):
                if indices[j] < i:
                    j += 1
                if j == len(indices):
                    break
                count += end - indices[j] + 1
            return count
        ans = 0
        start = 0
        curMax = -1

        for i in range(len(nums)):
            curMax = max(curMax, nums[i])
            if curMax > right:
                ans += countFunc(start, i - 1)
                curMax = -1
                start = i + 1
        ans += countFunc(start, len(nums) - 1)    
            
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        start = 0
        lastValidIdx = -1

        for i in range(len(nums)):
            if nums[i] > right:
                start = i + 1
                lastValidIdx = -1
                continue
            elif nums[i] >= left:
                lastValidIdx = i

            ans += max(lastValidIdx - start + 1, 0)
            
        return ans
    

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = cnt = 0
            for num in nums:
                cnt = cnt + 1 if num <= bound else 0
                ans += cnt
            return ans

        return count(right) - count(left - 1)