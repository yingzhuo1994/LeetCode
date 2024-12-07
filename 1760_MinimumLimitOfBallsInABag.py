# 1st solution
# O(n * log(m)) time | O(1) space
# where n = len(nums) and m = max(nums)
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        k = maxOperations
        start = 1
        end = max(nums)
        ans = end
        while start <= end:
            mid = start + (end - start) // 2
            count = 0
            for num in nums:
                if num > mid:
                    q, r = divmod(num, mid)
                    if r > 0:
                        q += 1
                    count += q - 1
                if count > k:
                    break
            if count > k:
                start = mid + 1
            else:
                ans = min(ans, mid)
                end = mid - 1
        
        return ans
