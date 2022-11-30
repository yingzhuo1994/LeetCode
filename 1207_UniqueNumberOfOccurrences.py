# 1st solution
# O(n) time | O(n) space
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freqSet = set(count.values())
        return len(count) == len(freqSet)