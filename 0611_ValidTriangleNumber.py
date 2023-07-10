# 1st solution, TLE
# O(n^3) time, O(1) space
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k] and abs(nums[i] - nums[j]) < nums[k]:
                        ans += 1
        return ans

# 2nd solution
# O(n^2 * log(n)) time, O(n) space
from math import factorial
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        count = Counter(nums)
        if 0 in count:
            count.pop(0)
        keys = list(count.keys())
        keys.sort()
        n = len(keys)
        sumArray = [count[num] for num in keys]
        for i in range(n - 1):
            sumArray[i + 1] += sumArray[i]

        for i in range(n):
            num1 = keys[i]
            v1 = count[num1]
            if count[num1] >= 3:
                val = factorial(v1) // (6 * factorial(v1 - 3))
                ans += val
            
            if count[num1] >= 2:
                idx = bisect.bisect_left(keys, num1 * 2)
                val = factorial(v1) // (2 * factorial(v1 - 2)) * (sumArray[idx - 1] - count[num1])
                ans += val
            
            for j in range(i + 1, n):
                num2 = keys[j]
                v2 = count[num2]
                idx = bisect.bisect_left(keys, num1 + num2)
                v3 = sumArray[idx - 1] - sumArray[j]
                val = v1 * v2 * v3
                ans += val
        
        return ans

# 3rd solution
# O(n^2) time, O(n) space
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(2, n):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count