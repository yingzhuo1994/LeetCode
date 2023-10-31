# 1st solution
# O(n) time | O(n) space
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = pref[:]
        for i in range(1, n):
            arr[i] = pref[i - 1] ^ pref[i]
        return arr