# 1st solution
# O(m + nk * log(m)) time | O(m + nk) space
# where m = len(s), n = len(words), and k is the average length of each word
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexDic = defaultdict(list)
        for i, ch in enumerate(s):
            indexDic[ch].append(i)
        
        ans = 0
        wordsCount = Counter(words)
        for word in wordsCount:
            ans += self.isSubsequence(word, indexDic) * wordsCount[word]
        return ans
    
    def isSubsequence(self, word, indexDic, i=0, lastIdx=-1):
        if i == len(word):
            return True
        ch = word[i]
        if ch not in indexDic:
            return False
        indices = indexDic[ch]
        idx = bisect.bisect_right(indices, lastIdx)
        if idx >= len(indices):
            return False
        if self.isSubsequence(word, indexDic, i + 1, indices[idx]):
            return True
        return False

# 2nd solution
# O(m + nk * log(m)) time | O(m + nk) space
# where m = len(s), n = len(words), and k is the average length of each word
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexDic = defaultdict(list)
        for i, ch in enumerate(s):
            indexDic[ch].append(i)
        
        wordsCount = Counter(words)
        trie = Trie()
        for word, k in wordsCount.items():
            trie.add(word, k)
        
        return trie.dfs(trie.dic, indexDic, -1)
    
class Trie:
    def __init__(self):
        self.dic = {}
        self.end = "*"
    
    def add(self, word, count):
        dic = self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = count
    
    def dfs(self, dic, indexDic, lastIdx):
        count = 0
        if self.end in dic:
            count += dic[self.end]
            dic[self.end] = 0
        for ch in dic:
            if ch not in indexDic:
                continue
            indices = indexDic[ch]
            idx = bisect.bisect_right(indices, lastIdx)
            if idx >= len(indices):
                continue
            count += self.dfs(dic[ch], indexDic, indices[idx])
        return count


