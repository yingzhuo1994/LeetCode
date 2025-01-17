# 1st solution
# O(n) time | O(1) space
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        val = 0
        for num in derived:
            val ^= num
        return val == 0