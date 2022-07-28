# 1st hash table solution
# O(n) time | O(1) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        for ch in t:
            if ch not in dic or dic[ch] == 0:
                return False
            else:
                dic[ch] -= 1
        return True

# 2nd sorting solution
# O(nlogn) time | O(1) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
