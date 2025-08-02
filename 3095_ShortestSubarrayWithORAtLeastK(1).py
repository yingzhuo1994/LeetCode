# 1st solution
# O(n) time | O(1) space 
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        start = 0
        ans = float("inf")
        cur = 0
        for i, num in enumerate(nums):
            d = 0
            cur |= num
            while num > 0:
                val = num & 1
                if val > 0:
                    dic[d] = dic.get(d, 0) + 1
                d += 1
                num >>= 1
            while cur >= k and start <= i:
                ans = min(ans, i - start + 1)
                num = nums[start]
                d = 0
                while num > 0:
                    val = num & 1
                    if val > 0:
                        dic[d] -= 1
                        if dic[d] == 0:
                            cur -= 1 << d
                    d += 1
                    num >>= 1
                start += 1
            if ans == 1:
                return ans
        return ans if ans != float("inf") else -1
            