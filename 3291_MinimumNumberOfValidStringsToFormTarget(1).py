# 1st solution
# O(n^2) time | O(n^2) space 
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        n = len(target)
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            if dp[i - 1] < 0:
                continue
            length = trie.check(target[i-1:])
            for j in range(length):
                dp[i + j] = dp[i - 1] + 1 if dp[i + j] < 0 else min(dp[i + j], dp[i - 1] + 1)
            if dp[n] >= 0:
                return dp[n]
        return dp[n]


class Trie:
    def __init__(self):
        self.dic = {}
    
    def add(self, word):
        dic = self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
    
    def check(self, word):
        length = 0
        dic = self.dic
        for ch in word:
            if ch in dic:
                dic = dic[ch]
                length += 1
            else:
                break
        return length