# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def distinctIntegers(self, n: int) -> int:
        visited = set([n])
        level = [n]
        while level:
            newLevel = []
            for num in level:
                for i in range(1, n + 1):
                    if num % i == 1 and i not in visited:
                        newLevel.append(i)
                        visited.add(i)
            level = newLevel
        return len(visited)

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            return n - 1