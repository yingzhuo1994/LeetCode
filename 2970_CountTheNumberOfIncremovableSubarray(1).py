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