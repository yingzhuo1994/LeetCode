# 1st solution
# O(n) time | O(n) space
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        dic = {}
        ans = set()
        for i in range(n - 10 + 1):
            seq = s[i:i+10]
            if seq not in dic:
                dic[seq] = i
            else:
                ans.add(seq)
        return list(ans)