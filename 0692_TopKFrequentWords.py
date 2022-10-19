# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCount = Counter(words)
        wordsFreq = [[word, freq] for word, freq in wordsCount.items()]
        wordsFreq.sort(key=lambda v: [-v[1], v[0]])
        ans = []
        for i in range(k):
            ans.append(wordsFreq[i][0])
        return ans
