# 1st solution
# O(n) time | O(n) space
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        dp = [nums[i + 1] > nums[i] and nums[i + 1] - nums[i] == 1 for i in range(n - 1)]
        count = sum(dp[:k - 1])
        ans = []
        for i in range(k - 1, n - 1):
            if count >= k - 1:
                ans.append(nums[i])
            else:
                ans.append(-1)
            if dp[i]:
                count += 1
            if dp[i - k + 1]:
                count -= 1
        if count >= k - 1:
            ans.append(nums[-1])
        else:
            ans.append(-1)
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        def compare(idx):
            return nums[idx + 1] > nums[idx] and nums[idx + 1] - nums[idx] == 1
        
        n = len(nums)
        count = 0
        for i in range(k - 1):
            count += compare(i)

        ans = []
        for i in range(k - 1, n - 1):
            if count >= k - 1:
                ans.append(nums[i])
            else:
                ans.append(-1)
            if compare(i):
                count += 1
            if compare(i - k + 1):
                count -= 1
        if count >= k - 1:
            ans.append(nums[-1])
        else:
            ans.append(-1)
        return ans