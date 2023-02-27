# 1st solution
class Solution:
    # O(n) time | O(n) space
    def __init__(self, w: List[int]):
        self.w = w[:]
        total = sum(w)
        self.w = [v / total for v in self.w]
        for i in range(len(self.w) - 1):
            self.w[i + 1] += self.w[i]
        
    # O(log(n)) time | O(1) space
    def pickIndex(self) -> int:
        p = random.random()
        index = bisect.bisect_left(self.w, p)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()