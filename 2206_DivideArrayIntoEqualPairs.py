# 1st solution
# O(n) time | O(n) space
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for v in cnt.values():
            if v & 1:
                return False
        return True