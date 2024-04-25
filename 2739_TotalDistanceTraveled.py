# 1st solution
# O(n) time | O(1) space
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0
        while mainTank >= 5:
            dist += 10 * 5
            mainTank -= 5
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1
        dist += mainTank * 10
        return dist