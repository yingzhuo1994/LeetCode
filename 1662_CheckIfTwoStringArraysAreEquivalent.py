# 1st solution
# O(n) time | O(n) space
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        s2 = "".join(word2)
        return s1 == s2

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1, w2 = 0, 0
        i, j = 0, 0
        while w1 < len(word1) and w2 < len(word2):
            if i < len(word1[w1]) and j < len(word2[w2]):
                if word1[w1][i] != word2[w2][j]:
                    return False
                i += 1
                j += 1
            else:
                if i >= len(word1[w1]):
                    w1 += 1
                    i = 0
                if j >= len(word2[w2]):
                    w2 += 1
                    j = 0
        return w1 == len(word1) and w2 == len(word2)