# O(n) time | O(1) space
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic = Counter(s)
        t_dic = Counter(t)
        for ch in t_dic:
            if ch not in s_dic or s_dic[ch] < t_dic[ch]:
                return ch
        