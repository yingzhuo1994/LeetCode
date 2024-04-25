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

# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5 or additionalTank == 0:
            return mainTank * 10

        q, r = divmod(mainTank, 5)
        return q * 5 * 10 + self.distanceTraveled(r + min(q, additionalTank), max(0, additionalTank - q))