# 1st solution, Set
# O(n) time | O(n) space
# where n is the length of s
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 1 << k:
            return False
        
        numberSet = set()
        for i in range(len(s) - k + 1):
            numberSet.add(s[i:i+k])
            if len(numberSet) == 1 << k:
                return True

        return False

# 2nd solution, Rolling Hash
# O(n) time | O(2**k) space
# where n is the length of s
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) - k + 1 < need:
            return False
        
        got = [False]*need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False