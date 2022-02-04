# 1st solution, TLE
# O(n^2) time | O(n) space 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in reversed(range(i + 1, len(nums))):
                count = sum(nums[i:j+1])
                if count * 2 == j + 1 - i:
                    ans = max(ans, count * 2)
        return ans

# 2nd solution, TLE
# O(n) time | O(n) space 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-2] * (2 * len(nums) + 1)
        arr[len(nums)] = -1
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if arr[count + len(nums)] >= -1:
                maxlen = max(maxlen, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i
        return maxlen