# 1st solution
# O(n) time | O(n) space
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt1 = Counter(target)
        cnt2 = Counter(arr)
        for key in cnt1:
            if cnt1[key] != cnt2[key]:
                return False
        return True