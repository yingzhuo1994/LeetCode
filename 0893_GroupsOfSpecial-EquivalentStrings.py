# 1st solution
# O(kn) time | O(kn) space
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def getKey(word):
            odd = ""
            even = ""
            for i, ch in enumerate(word):
                if i & 1:
                    odd += ch
                else:
                    even += ch
            odd = sorted(odd)
            even = sorted(even)
            key = odd + even
            return "".join(key)
        n = len(words)
        dic = {}
        for word in words:
            key = getKey(word)
            dic[key] = dic.get(key, 0) + 1
        return len(dic)