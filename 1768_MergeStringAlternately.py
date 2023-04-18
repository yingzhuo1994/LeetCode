# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        stack = []
        while i < len(word1) and j < len(word2):
            stack.append(word1[i])
            i += 1
            stack.append(word2[j])
            j += 1
        stack.append(word1[i:] or word2[j:])
        ans = "".join(stack)
        return ans