# 1st solution
# O(n) time | O(n) space
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if 0 in cnt and cnt[0] > 1:
            return True
        for num in cnt:
            double = num * 2
            if double in cnt and double != 0:
                return True
        return False