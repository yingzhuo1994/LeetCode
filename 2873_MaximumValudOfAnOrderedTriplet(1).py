# 1st solution
# O(n^3) time | O(1) space
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val = (nums[i] - nums[j]) * nums[k]
                    ans = max(ans, val)
        return ans


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        val1 = nums[:]
        for i in range(1, n):
            val1[i] = max(val1[i - 1], nums[i])
        val3 = nums[:]
        for i in reversed(range(n - 1)):
            val3[i] = max(val3[i], val3[i + 1])
        for i in range(1, n - 1):
            val = (val1[i - 1] - nums[i]) * val3[i + 1]
            ans = max(ans, val)
        return ans