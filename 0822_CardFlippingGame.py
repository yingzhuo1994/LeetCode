# 1st solution
# O(n) time | O(n) space
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        impossible = set()
        for a, b in zip(fronts, backs):
            if a == b:
                impossible.add(a)
        ans = float("inf")
        for a, b in zip(fronts, backs):
            if a < ans and a not in impossible:
                ans = a
            if b < ans and b not in impossible:
                ans = b
        if ans == float("inf"):
            return 0
        return ans