# 1st solution
# O(n) time | O(n) space
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        ans = 0
        for ch in count2:
            if count2[ch] == 1 and count1.get(ch, 0) == 1:
                ans += 1
        return ans