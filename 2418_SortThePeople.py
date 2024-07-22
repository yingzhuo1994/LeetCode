# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = [[name, height] for name, height in zip(names, heights)]
        pairs.sort(lambda v: -v[1])
        return [name for name, height in pairs]
