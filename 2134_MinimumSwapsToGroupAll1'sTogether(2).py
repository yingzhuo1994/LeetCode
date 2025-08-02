# 1st solution
# O(n * log(n)) time | O(n) space
import collections
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = collections.deque()
        for i, num in enumerate(nums):
            if num == 1:
                ones.append(i)
        n = len(nums)
        k = len(ones)
        if k <= 1:
            return 0
        ans = n

        for _ in range(k):
            last = ones[0] + k - 1
            idx = bisect.bisect_right(ones, last)
            ans = min(ans, k - idx)
            if ans == 0:
                break
            i = ones.popleft()
            ones.append(i + n)
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        if k <= 1:
            return 0
        n = len(nums)
        count = 0
        for i in range(k):
            if nums[i] == 1:
                count += 1
        ans = k - count
        for i in range(1, n):
            count -= nums[i - 1] == 1
            count += nums[(i + k - 1) % n] == 1
            ans = min(ans, k - count)
        return ans