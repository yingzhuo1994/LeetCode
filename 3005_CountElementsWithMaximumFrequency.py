# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxFreq = max(counts.values())
        return sum(filter(lambda x: x == maxFreq, counts.values()))