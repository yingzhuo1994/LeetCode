# 1st solution
# O(n) time | O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = n // 3
        count = collections.Counter(nums)
        ans = []
        for k, v in count.items():
            if v > freq:
                ans.append(k)
        return ans