# 1st solution
# O(n) time | O(1) space
class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCount = 0
        lateCount = 0

        for ch in s:
            if ch == "A":
                absentCount += 1
            if ch == "L":
                lateCount += 1
            else:
                lateCount = 0
            if absentCount >= 2 or lateCount >= 3:
                return False
        return True

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') == 0