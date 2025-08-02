# 1st solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans =[0 for _ in range(n)]
        count = 0
        curSum = 0
        for i in range(n):
            ans[i] += curSum
            count += (boxes[i] == "1")
            curSum += count
        count = 0
        curSum = 0
        for i in reversed(range(n)):
            ans[i] += curSum
            count += (boxes[i] == "1")
            curSum += count
        return ans