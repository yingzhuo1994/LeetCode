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

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        letters = set(list(s))
        for letter in letters:
            lst = [-1]
            for i, ch in enumerate(s):
                if ch == letter:
                    lst.append(i)
                    if len(lst) >= 3:
                        ans += (lst[1] - lst[0]) * (lst[2] - lst[1])
                        lst.pop(0)
            lst.append(len(s))
            if len(lst) >= 3:
                ans += (lst[1] - lst[0]) * (lst[2] - lst[1])
                lst.pop(0)
        return ans


# 4th solution
# O(n) time | O(1) space
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = total = 0
        last0, last1 = {}, {}
        for i, c in enumerate(s):
            total += i - 2 * last0.get(c, -1) + last1.get(c, -1)
            ans += total
            last1[c] = last0.get(c, -1)
            last0[c] = i
        return ans