# 1st solution
# O(n) time | O(n) space
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ops = [0 for _ in range(len(s) + 1)]
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            ops[start] += val
            ops[end + 1] -= val 
        curOps = 0
        lst = list(s)
        for i in range(len(s)):
            curOps += ops[i]
            val = ord(s[i]) - ord("a") + curOps
            val %= 26
            ch = chr(ord("a") + val)
            lst[i] = ch
        return "".join(lst)