# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cnt = {}
        for i, num in enumerate(nums):
            if num not in cnt:
                cnt[num] = []
            cnt[num].append(i)
        ans = 0
        for num in cnt:
            lst = cnt[num]
            if len(lst) <= ans:
                continue
            start = 0
            last = lst[0] - 1
            left = k
            for i, idx in enumerate(lst):
                left -= idx - last - 1
                while left < 0:
                    left += lst[start+1] - lst[start] - 1
                    start += 1
                last = idx
                length = i - start + 1
                ans = max(ans, length)
        return ans
