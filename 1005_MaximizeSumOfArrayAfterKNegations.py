# 1st solution
# O(n) time | O(1) space
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        for val in range(-100, 0):
            if cnt[val] > 0:
                m = min(cnt[val], k)
                cnt[-val] += m
                cnt[val] -= m
                k -= m
            if k == 0:
                break
        if k & 1:
            for val in range(0, 101):
                if cnt[val] > 0:
                    cnt[-val] += 1
                    cnt[val] -= 1
                    break
        ans = 0
        for val, freq in cnt.items():
            ans += val * freq
        return ans