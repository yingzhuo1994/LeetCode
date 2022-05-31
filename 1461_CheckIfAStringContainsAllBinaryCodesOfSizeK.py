# 1st solution
# O(n) time | O(n) space
# where n is the length of s
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 2**k:
            return False
        
        numberSet = set()
        for i in range(len(s) - k + 1):
            num = int(s[i:i+k], 2)
            numberSet.add(num)

        return len(numberSet) == 2**k