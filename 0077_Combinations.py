# 1st solution
# O(n!/(k!*(n-k)!)) time | O(n!/((k-1)!*(n-k)!)) space
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        result = []
        for i in reversed(range(k, n + 1)):
            last = self.combine(i - 1, k - 1)
            result += [[i] + lst for lst in last]
        return result

# 2nd solution
# O(n!/(k!*(n-k)!)) time | O(n!/((k-1)!*(n-k)!)) space
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        
        withLast = self.combine(n - 1, k - 1)
        withoutLast = self.combine(n - 1, k)
        ans = [lst + [n] for lst in withLast] + withoutLast
        return ans