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
