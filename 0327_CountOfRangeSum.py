# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        array = [0]
        for i in range(n):
            array.append(array[-1] + nums[i])
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                curSum = array[i] - array[j - 1]
                if lower <= curSum <= upper:
                    ans += 1
        return ans