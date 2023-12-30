# 1st solution
# O(n) time | O(1) space
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for word in words:
            for ch in word:
                dic[ch] = dic.get(ch, 0) + 1
        n = len(words)
        for value in dic.values():
            if value % n != 0:
                return False
        return True