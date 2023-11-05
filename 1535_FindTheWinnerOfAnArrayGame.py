# 1st solution
# O(n) time | O(1) space
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if cur > arr[i]:
                count += 1
            else:
                cur = arr[i]
                count = 1
            if count >= k:
                return cur
        return cur