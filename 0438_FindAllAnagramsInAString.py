# 1st solution
# O(n) time | O(1) space
# where n is the length of s
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        goalDic = {}
        for ch in p:
            goalDic[ch] = goalDic.get(ch, 0) + 1
        validLength = len(p)
        curLength = 0
        ans = []
        dic = {}
        for i in reversed(range(len(s))):
            ch = s[i]
            if i + validLength < len(s):
                lastCh = s[i + validLength]
                if lastCh in dic and lastCh in goalDic:
                    dic[lastCh] -= 1
                    if dic[lastCh] < goalDic[lastCh]:
                        curLength -= 1
            dic[ch] = dic.get(ch, 0) + 1
            if ch in goalDic and dic[ch] <= goalDic[ch]:
                curLength += 1
            if curLength == validLength:
                ans.append(i)

        return ans[::-1]