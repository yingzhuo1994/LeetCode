# 1st solution
# O(n) time | O(n) space
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.split()
        def getWord(word):
            if len(word) == 0:
                return []
            ans = []
            for ch in "!?',;.":
                if ch in word:
                    lst = word.split(ch)
                    for w in lst:
                        ans.extend(getWord(w))
                    return ans
            ans.append(word)
            return ans
        counts = {}
        banned = set([w.lower() for w in banned])
        for word in words:
            lst = getWord(word)
            for w in lst:
                w = w.lower()
                if w not in banned:
                    counts[w] = counts.get(w, 0) + 1
        ans, freq = None, 0
        for k, v in counts.items():
            if v > freq:
                freq = v
                ans = k
        return ans