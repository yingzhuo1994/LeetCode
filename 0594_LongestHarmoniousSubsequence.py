# 1st solution
# O(n) time | O(n) space
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for num in count:
            if (num + 1) not in count:
                continue
            v1 = count[num] + count[num + 1]
            ans = max(ans, v1)
        return ans