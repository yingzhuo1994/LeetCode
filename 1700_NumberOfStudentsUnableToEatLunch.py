# 1st solution
# O(n) time | O(1) space
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                counts[sandwich] -= 1
            else:
                return sum(counts.values())
        return 0