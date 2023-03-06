# 1st solution
# O(n) time | O(1) space
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        cur = 1
        for num in arr:
            if num > cur:
                diff = num - cur
                if count + diff >= k:
                    return cur + k - count - 1
                count += diff
            cur = num + 1
        diff = k - count
        return cur + diff - 1