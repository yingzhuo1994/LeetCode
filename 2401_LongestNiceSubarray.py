# 1st solution
# O(n * log(k) * k^2) time | O(1) space
# where k = 32
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check(a, b):
            for i in range(a, b):
                for j in range(i + 1, b):
                    if (nums[i] & nums[j]) != 0:
                        return False
            return True

        n = len(nums)
        start = 1
        end = 32
        ans = 1
        while start <= end:
            mid = start + (end - start) // 2
            isValid = False
            for i in range(n - mid + 1):
                isValid = check(i, i + mid)
                if isValid:
                    break
            if isValid:
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans