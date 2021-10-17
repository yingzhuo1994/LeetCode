class Solution:
    # 1st solution
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        result = []
        for i in reversed(range(k, n + 1)):
            last = self.combine(i - 1, k - 1)
            result += [[i] + lst for lst in last]
        return result