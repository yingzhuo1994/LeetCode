# 1st solution
# O(n) time | O(n) space
class Solution:
    def average(self, salary: List[int]) -> float:
        count = collections.Counter(salary)
        minSalary = min(list(count.keys()))
        maxSalary = max(list(count.keys()))
        if minSalary == maxSalary:
            return 0.0
        total = sum(salary)
        n = len(salary)
        total -= count[minSalary] * minSalary + count[maxSalary] * maxSalary
        n -= count[minSalary] + count[maxSalary]
        average = total / n
        return average