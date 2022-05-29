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

# 2nd solution, Bitmask
# O(n^2) time | O(n) space
class Solution:
    def maxProduct(self, words):
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans

# 3rd solution, Improved Bitmask
# O(n^2) time | O(n) space
class Solution:
    def maxProduct(self, words):
        dic = defaultdict(int)
        ans = 0

        for word in words:
            keyBit = 0
            for l in word:
                keyBit |= 1<<(ord(l) - 97)
            dic[keyBit] = max(dic.get(keyBit, 0), len(word))

        for k1, k2 in combinations(dic.keys(), 2):
            if k1 & k2 == 0: 
                ans = max(ans, dic[k1]*dic[k2])
                
        return ans