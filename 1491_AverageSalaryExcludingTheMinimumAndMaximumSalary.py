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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        minSalary = salary[0]
        maxSalary = salary[0]
        for s in salary:
            total += s
            minSalary = min(minSalary, s)
            maxSalary = max(maxSalary, s)
        total -= minSalary + maxSalary
        n = len(salary) - 2
        return total / n