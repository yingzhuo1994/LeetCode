# 1st solution
# O(n) time | O(n) space
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for i, word in enumerate(words):
            if len(word) > 1 and word.startswith("$") and word[1] not in ["0", "-"] and word[1:].isdigit():
                val = int(word[1:])
                if val > 0:
                    val = (100 - discount) / 100 * val
                    words[i] = f"${val:.2f}"
        return " ".join(words)
