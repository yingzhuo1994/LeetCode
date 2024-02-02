# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def stoneGameVI(self, a: List[int], b: List[int]) -> int:
        pairs = sorted(zip(a, b), key=lambda p: -p[0] - p[1])
        diff = sum(x if i % 2 == 0 else -y for i, (x, y) in enumerate(pairs))
        return (diff > 0) - (diff < 0)