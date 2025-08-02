# 1st solution
# O(n) time | O(n) space
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos

    def query(self, left: int, right: int, value: int) -> int:
        a = self.pos[value]
        return bisect_right(a, right) - bisect_left(a, left)