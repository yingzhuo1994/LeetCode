# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        if mx >= k:
            return 1
        if mx * 10 < k:
            return -1
        val = 0
        for num in nums:
            val |= num
  
        if val < k:
            return -1
        dic = {i: 0 for i in range(32)}
        start = 0
        cur = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            cur |= num
            d = 0
            while num > 0:
                if num & 1:
                    dic[d] += 1
                num >>= 1
                d += 1
            while cur >= k:
                ans = min(ans, i - start + 1)
                num = nums[start]
                d = 0
                while num > 0:
                    if num & 1:
                        dic[d] -= 1
                        if dic[d] == 0:
                            cur ^= 1 << d
                    num >>= 1
                    d += 1
                start += 1
        return ans