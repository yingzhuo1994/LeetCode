# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.dic = {}
        words.sort(key=lambda v: [len(v), v])
        ans = ""
        for word in words:
            if self.build(word) and len(word) > len(ans):
                ans = word

        return ans
    
    def build(self, word):
        dic = self.dic
        if len(word) == 1:
            if word not in dic:
                dic[word] = {}
            return True
        
        for i in range(len(word) - 1):
            if word[i] not in dic:
                return False
            dic = dic[word[i]]
        if word[-1] not in dic:
            dic[word[-1]] = {}
        
        return True