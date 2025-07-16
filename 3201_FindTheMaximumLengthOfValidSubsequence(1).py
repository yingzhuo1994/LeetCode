# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 2
        cnt = 0
        last = 1
        for num in nums:
            if last:
                if num & 1:
                    continue
                else:
                    cnt += 1
                    last ^= 1
            else:
                if num & 1:
                    cnt += 1
                    last ^= 1
                else:
                    continue
        ans = max(ans, cnt)
        cnt = 0
        last = 0
        for num in nums:
            if last:
                if num & 1:
                    continue
                else:
                    cnt += 1
                    last ^= 1
            else:
                if num & 1:
                    cnt += 1
                    last ^= 1
                else:
                    continue
        ans = max(ans, cnt)

        odd = 0
        even = 0
        for num in nums:
            if num & 1:
                odd += 1
            else:
                even += 1
        ans = max(ans, odd, even)
        return ans