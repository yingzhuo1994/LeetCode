# 1st solution
# O(n) time | O(1) space
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        val = 0
        for num in nums:
            val <<= 1
            val |= num
            if val % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans