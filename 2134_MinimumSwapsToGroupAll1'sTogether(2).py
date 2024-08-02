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