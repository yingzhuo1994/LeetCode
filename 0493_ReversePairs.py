# 1st solution, TLE
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        memo = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    memo[i] = max(memo.get(i, 0), memo.get(j, 0)) + 1
        return sum([memo.values()])

# 2nd solution
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return self.mergesort(nums)[1]
       
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums, 0
        m = len(nums) // 2
        left, countl = self.mergesort(nums[:m])
        right, countr = self.mergesort(nums[m:])
        count = countl + countr
        for r in right:
            temp = len(left) - bisect.bisect(left, 2*r)
            if temp == 0:
                break
            count += temp
        
        return sorted(left + right), count    