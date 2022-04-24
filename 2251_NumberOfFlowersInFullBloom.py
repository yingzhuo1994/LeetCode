class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end = sorted(a for a,b in flowers), sorted(b for a,b in flowers)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]