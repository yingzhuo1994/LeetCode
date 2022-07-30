# 1st solution
# O(n) time | O(n) space
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subDic = Counter()
        for word in words2:
            count = Counter(word)
            for ch in count:
                subDic[ch] = max(subDic[ch], count[ch])
        
        ans = []
        for word in words1:
            count = Counter(word)
            if all(count[ch] >= subDic[ch] for ch in subDic):
                ans.append(word)
        return ans
