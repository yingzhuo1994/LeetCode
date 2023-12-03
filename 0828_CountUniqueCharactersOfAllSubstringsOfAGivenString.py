# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        for length in range(1, len(s) + 1):
            dic = Counter(s[:length])
            uniqueCount = 0
            for ch in dic:
                if dic[ch] == 1:
                    uniqueCount += 1
            ans += uniqueCount
            for i in range(length, len(s)):
                ch = s[i]
                if dic.get(ch, 0) == 0:
                    uniqueCount += 1
                elif dic.get(ch, 0) == 1:
                    uniqueCount -= 1
                dic[ch] = dic.get(ch, 0) + 1
                ch1 = s[i - length]
                dic[ch1] -= 1
                if dic[ch1] == 0:
                    uniqueCount -= 1
                elif dic[ch1] == 1:
                    uniqueCount += 1
                
                ans += uniqueCount
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {ch: [-1, -1] for ch in string.ascii_uppercase}
        res = 0
        for i, ch in enumerate(s):
            left, right = index[ch]
            res += (right - left) * (i - right)
            index[ch] = [right, i]
        for ch in index:
            left, right = index[ch]
            res += (right - left) * (len(s) - right)
        return res % (10**9 + 7)