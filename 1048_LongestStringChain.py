# 1st solution
# O(n*log(n) + n*L) time | O(n) space
# where n is the length of words, and L is the average lenth of words[i].length
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        wordDic = {word: 1 for word in words}
        ans = 1
        for i in reversed(range(len(words))):
            word = words[i]
            for j in range(len(word)):
                newWord = word[:j] + word[j+1:]
                if newWord in wordDic:
                    wordDic[newWord] = max(wordDic[newWord], wordDic[word] + 1)
                    ans = max(ans, wordDic[newWord])
        return ans