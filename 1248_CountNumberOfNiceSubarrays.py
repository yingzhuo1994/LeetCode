# 1st solution
# O(n) time | O(n) space
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        ans = 0
        freq = 0
        for num in nums:
            if num & 1:
                freq += 1
            dic[freq] = dic.get(freq, 0) + 1
            ans += dic.get(freq - k, 0)
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = count = res = 0
        for j in range(len(nums)):
            if nums[j] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            res += count
        return res