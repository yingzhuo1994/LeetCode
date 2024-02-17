# 1st solution
# O(kn) time | O(1) space
# where n = len(words), k is the longest length of word in words
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counts = Counter(licensePlate.lower())
        ans = ""

        for word in words:
            dic = Counter(word.lower())

            valid = True
            for ch in counts:
                if not ch.isalpha():
                    continue
                if dic[ch] < counts[ch]:
                    valid = False
                    break

            if valid and (ans == "" or len(word) < len(ans)):
                ans = word
        
        return ans