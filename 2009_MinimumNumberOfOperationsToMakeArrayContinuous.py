# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dic = Counter(nums)
        minVal, maxVal = min(nums), max(nums)
        diff = maxVal - minVal
        if diff <= n - 1:
            return n - len(dic)
        else:
            nums.sort()
            ans = n
            for i, num in enumerate(nums):
                idx = bisect.bisect_left(nums, num + n)
                valid = len(set(nums[i:idx]))
                ans = min(ans, n - valid)
                if idx == n:
                    break
            return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        minVal, maxVal = min(nums), max(nums)
        diff = maxVal - minVal
        if diff <= n - 1:
            dic = Counter(nums)
            return n - len(dic)
        else:
            nums.sort()
            ans = n
            dic = {}
            last = 0
            for i, num in enumerate(nums):
                idx = bisect.bisect_left(nums, num + n)
                if last < idx:
                    for j in range(last, idx):
                        dic[nums[j]] = dic.get(nums[j], 0) + 1
                if i > 0:
                    dic[nums[i - 1]] -= 1
                    if dic[nums[i - 1]] == 0:
                        dic.pop(nums[i - 1])

                valid = len(dic)
                ans = min(ans, n - valid)
                last = idx
                if idx == n:
                    break
            return ans