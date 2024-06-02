# 1st solution
# O(n) time | O(n) space
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt1 = Counter(s1.split())
        cnt2 = Counter(s2.split())
        ans = []
        for word in cnt1:
            if word not in cnt2 and cnt1[word] == 1:
                ans.append(word)
        for word in cnt2:
            if word not in cnt1 and cnt2[word] == 1:
                ans.append(word)
        return ans

# 1st solution
# O(n) time | O(n) space
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + " " + s2).split())
        return [word for word in cnt if cnt[word] == 1]