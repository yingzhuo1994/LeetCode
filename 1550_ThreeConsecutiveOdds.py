# 1st solution
# O(n) time | O(1) space
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num & 1:
                count += 1
            else:
                count = 0
            if count >= 3:
                return True
        return False