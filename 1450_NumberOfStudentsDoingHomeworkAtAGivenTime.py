# 1st solution
# O(n) time | O(1) space
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        return count