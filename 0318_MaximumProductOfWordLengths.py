# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            keyWord = "".join(sorted(list(set(word))))
            dic[keyWord] = max(dic.get(keyWord, 0), len(word))
        keyWords = list(dic.keys())
        ans = 0
        for i in range(len(keyWords)):
            for j in range(i):
                if self.notShare(keyWords[i], keyWords[j]):
                    ans = max(ans, dic[keyWords[i]] * dic[keyWords[j]])
        return ans
    
    def notShare(self, s, t):
        s_set = set(s)
        for ch in t:
            if ch in s_set:
                return False
        return True