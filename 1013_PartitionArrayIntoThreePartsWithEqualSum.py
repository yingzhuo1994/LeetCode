# 1st solution
# O(n) time | O(1) space
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        curSum = 0
        cnt = 0
        for num in arr:
            curSum += num
            if curSum == target:
                cnt += 1
                curSum = 0
        return cnt >= 3