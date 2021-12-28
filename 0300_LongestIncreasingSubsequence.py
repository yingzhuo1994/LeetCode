# 1st solution, dynamic programming
# O(n^2) time | O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        countLst = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    countLst[i] = max(countLst[j] + 1, countLst[i])
        return max(countLst)

# 2nd solution, intelligently build a subsequence
# O(n^2) time | O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

# 3rd solution, imporve with binary search
# O(nlogn) time | O(n) space
# In Python, the bisect module provides super handy functions that does binary search for us.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace the first element in sub greater than num
            else:
                sub[i] = num
        
        return len(sub)