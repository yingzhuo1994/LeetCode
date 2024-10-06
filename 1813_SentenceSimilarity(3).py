# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        prefix = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                break
            prefix = i
        if prefix == len(s1) - 1:
            return True
        suffix = -1
        for i in range(1, len(s1) + 1):
            if s1[-i] != s2[-i]:
                break
            suffix = i
        if suffix == len(s1):
            return True

        return prefix + suffix >= len(s1) - 1
        