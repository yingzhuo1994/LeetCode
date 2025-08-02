# 1st solution
# O(n^3) time | O(n) space
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def isIncreasingArray(array):
            for i in range(1, len(array)):
                if array[i-1] >= array[i]:
                    return False
            return True
        ans = 0
        n = len(nums)
        for i in range(n):
            if i == 0:
                front = []
            else:
                front = nums[:i]
            for j in range(i, n):
                if j == n - 1:
                    back = []
                else:
                    back = nums[j+1:]
                array = front + back
                ans += isIncreasingArray(array)
        return ans

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        prefix = [True] * (n + 1)
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                for j in range(i + 1, n):
                    prefix[j] = False
                break
        suffix = [True] * (n + 1)
        for i in reversed(range(n - 1)):
            if nums[i] >= nums[i+1]:
                for j in reversed(range(i)):
                    suffix[j] = False
                break

        for i in range(n):
            if not prefix[i]:
                break
            for j in reversed(range(i, n)):
                if not suffix[j]:
                    break
                if i == 0 or j == n - 1:
                    ans += 1
                else:
                    ans += nums[i - 1] < nums[j + 1]
        return ans