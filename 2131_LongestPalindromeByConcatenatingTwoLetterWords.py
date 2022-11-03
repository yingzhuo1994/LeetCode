# 1st solution
# O(n) time | O(n) space
import collections
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_dic = collections.Counter(words)
        centerCount = 0
        plusOne = 0
        partCount = 0
        for word in words_dic:
            if word[:] == word[::-1]:
                if words_dic[word] % 2 == 1:
                    plusOne = 1
                centerCount += (words_dic[word] // 2) * 2
            elif word[::-1] in words_dic:
                partCount += min(words_dic[word], words_dic[word[::-1]])
        return (centerCount + plusOne + partCount) * 2

