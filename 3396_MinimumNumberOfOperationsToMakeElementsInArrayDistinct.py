# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        k = 0
        for num in cnt:
            if cnt[num] > 1:
                k += 1
        ans = 0
        i = 0
        while k > 0:
            for j in range(i, min(i + 3, len(nums))):
                cnt[nums[j]] -= 1
                if cnt[nums[j]] == 1:
                    k -= 1
            i += 3
            ans += 1
        return ans