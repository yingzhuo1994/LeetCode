# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxFreq = max(counts.values())
        ans = 0
        for freq in counts.values():
            if freq == maxFreq:
                ans += maxFreq
        return ans