# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        minNum = n - 1
        count = 0
        for i in reversed(range(n)):
            num = arr[i]
            if num < minNum:
                minNum = num
            count += 1
            if count == n - minNum:
                ans += 1
        return ans
