# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = sum(abs(a - b) for a, b in zip(seats, students))
        return ans