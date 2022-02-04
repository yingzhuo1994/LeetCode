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

# 2nd solution
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

# 3rd solution
# O(n) time | O(n) space 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length