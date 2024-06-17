# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        ans = 0
        mask1 = 0
        mask2 = 0
        dic = {}
        for i, num in enumerate(arr):
            idx = bisect.bisect_left(sorted_arr, num, lo=dic.get(num, 0))
            mask1 |= 1 << idx
            mask2 |= 1 << i
            dic[num] = idx + 1

            if mask1 == mask2:
                ans += 1
        return ans