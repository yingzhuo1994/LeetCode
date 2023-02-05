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

# 2nd solution
# O(n) time | O(1) space
# where n is the length of s
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        if n < k:
            return []
        dic_p = Counter(p)
        valid = 0
        unique = len(dic_p)
        start = 0
        dic = Counter()
        ans = []
        for i in range(n):
            ch = s[i]
            dic[ch] += 1
            if dic[ch] == dic_p[ch]:
                valid += 1
            while i - start + 1 > k:
                ch = s[start]
                if dic[ch] == dic_p[ch]:
                    valid -= 1
                dic[ch] -= 1
                start += 1
            if valid == unique:
                ans.append(start)
        return ans