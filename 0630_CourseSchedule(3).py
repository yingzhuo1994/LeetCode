# O(n*logn) time | O(n) space
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        legalCourse = [[a, b] for a, b in courses if a <= b]
        legalCourse.sort(key = lambda v: [v[1], v[0]])
        stack = []
        totalTime = 0
        courseNumber = 0
        for duration, endTime in legalCourse:
            if totalTime + duration <= endTime:
                courseNumber += 1
                totalTime += duration
                heapq.heappush(stack, -duration)
            else:
                if -stack[0] > duration:
                    totalTime += heapq.heappop(stack)
                    totalTime += duration
                    heapq.heappush(stack, -duration)

        return courseNumber