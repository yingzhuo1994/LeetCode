# 1st solution
# O(n) time | O(1) space
# where n is the length of s
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        targetDic = Counter(p)
        dic = {}
        count = 0
        goalLength = len(p)
        ans = []
        for i in range(len(s)):
            front = i - goalLength
            if front >= 0:
                dic[s[front]] -= 1
                if s[front] in targetDic and dic[s[front]] < targetDic[s[front]]:
                    count -= 1
            dic[s[i]] = dic.get(s[i], 0) + 1
            if s[i] in targetDic and dic[s[i]] <= targetDic[s[i]]:
                count += 1
            if count == goalLength:
                ans.append(front + 1)
        return ans