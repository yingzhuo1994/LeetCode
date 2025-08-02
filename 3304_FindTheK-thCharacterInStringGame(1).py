# 1st solution
# O(log(k)) time | O(1) space
class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'
        elif k == 2:
            return 'b'
        n = k.bit_length() - 1
        if k == pow(2, n):
            m = (ord(self.kthCharacter(k >> 1)) + 1 - ord("a")) % 26
        else:
            m = (ord(self.kthCharacter(k - pow(2, n))) + 1 - ord("a")) % 26
        return chr(ord("a") + m)