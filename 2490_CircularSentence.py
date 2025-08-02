# 1st solution
# O(n) time | O(n) space
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split()
        for i in range(len(lst)):
            if lst[i-1][-1] != lst[i][0]:
                return False
        return True