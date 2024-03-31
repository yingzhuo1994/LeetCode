# 1st solution
# O(n) time | O(n) space
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        ans = []
        for i, word in enumerate(words, 1):
            if word[0].lower() in "aeiou":
                new = word + "ma" + ("a" * i)
            else:
                new = word[1:] + word[0] + "ma" + ("a" * i)
            ans.append(new)
        return " ".join(ans)