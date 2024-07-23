# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        pairs = list(cnt.items())
        pairs.sort(key=lambda v: [v[1], -v[0]])
        ans = []
        for key, freq in pairs:
            ans += [key] * freq
        return ans;