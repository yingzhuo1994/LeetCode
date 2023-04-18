# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        stack = []
        while i < len(word1) and i < len(word2):
            stack.append(word1[i])
            stack.append(word2[i])
            i += 1
        stack.append(word1[i:] or word2[i:])
        ans = "".join(stack)
        return ans

# 2nd solution
# O(m + n) time | O(m + n) space
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))