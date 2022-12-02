# 1st solution
# O(n) time | O(n) space
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        if len(count1) != len(count2):
            return False

        if count1 == count2:
            return True

        for ch in count1:
            if ch not in count2:
                return False
        
        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())
        return freq1 == freq2