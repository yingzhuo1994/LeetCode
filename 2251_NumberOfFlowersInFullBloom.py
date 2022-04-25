# 1st solution, Binary Search
# O(n*log(n) + m*log(m)) time | O(n) space
# where n is the length of flowers, and m is the length of persons
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end = sorted(a for a,b in flowers), sorted(b for a,b in flowers)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]

# 2nd solution
# O(n*log(n) + m*log(m)) time | O(n) space
# where n is the length of flowers, and m is the length of persons
import sortedcontainers
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = sortedcontainers.SortedDict({0: 0})
        for i, j in flowers:
            diff[i] = diff.get(i, 0) + 1
            diff[j + 1] = diff.get(j + 1, 0) - 1
        
        count = list(accumulate(diff.values()))
        return [count[diff.bisect(t) - 1] for t in persons]