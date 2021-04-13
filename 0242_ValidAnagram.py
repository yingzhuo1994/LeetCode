class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for ch in t:
            if ch not in dic or dic[ch] == 0:
                return False
            else:
                dic[ch] -= 1
        return True

        # 2n one-line solution
        return sorted(s) == sorted(t)
