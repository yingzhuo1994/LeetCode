# 1st solution
# O(n) time | O(n) space
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = pref[:]
        for i in range(1, n):
            arr[i] = pref[i - 1] ^ pref[i]
        return arr

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        for i in reversed(range(1, n)):
            pref[i] ^= pref[i - 1]
        return pref