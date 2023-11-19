# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        keys = sorted(list(count.keys()))
        ans = 0
        for i in reversed(range(1, len(keys))):
            ans += count[keys[i]]
            count[keys[i - 1]] += count[keys[i]]
        return ans