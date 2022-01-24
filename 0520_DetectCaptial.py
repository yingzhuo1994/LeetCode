# 1st solution
# O(n) time | O(1) space
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        isFirstCapital = word[0].upper() == word[0]
        isSecondCapital = word[1].upper() == word[1]
        if isFirstCapital and isSecondCapital:
            for i in range(2, len(word)):
                if word[i].upper() != word[i]:
                    return False
        else:
            for i in range(1, len(word)):
                if word[i].upper() == word[i]:
                    return False
        return True