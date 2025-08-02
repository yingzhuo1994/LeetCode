# 1st solution
# O(n) time | O(n) space
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        pair = 0
        ans = 0
        start = 0
        n = len(nums)
        for i, num in enumerate(nums):
            cnt[num] += 1
            pair += cnt[num] - 1

            while pair >= k:
                ans += n - i
                cnt[nums[start]] -= 1
                pair -= cnt[nums[start]]
                start += 1 

        return ans