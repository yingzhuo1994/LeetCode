# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda v: [bin(v).count("1"), v])
        return arr