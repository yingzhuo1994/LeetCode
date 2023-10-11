# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        points = []
        for s, id in zip(report, student_id):
            words = s.split()
            cur = 0
            for word in words:
                if word in positive_feedback:
                    cur += 3
                elif word in negative_feedback:
                    cur -= 1
            points.append([cur, id])
        
        points.sort(key = lambda v: [-v[0], v[1]])
        return [points[i][1] for i in range(k)]