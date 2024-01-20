# 1st solution
# O(n) time | O(n) space
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            lst = word.split(separator)
            ans.extend([w for w in lst if len(w) > 0])
        return ans