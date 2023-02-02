# 1st solution
# O(n) time | O(1) space
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, ch in enumerate(order):
            dic[ch] = i
        
        def compare(a, b):
            if a == b:
                return 0
            i, j = 0, 0
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            if j == len(b) or i < len(a) and dic[a[i]] > dic[b[j]]:
                return 1
            return -1

        n = len(words)
        for i in range(n - 1):
            if compare(words[i], words[i + 1]) > 0:
                return False
        return True