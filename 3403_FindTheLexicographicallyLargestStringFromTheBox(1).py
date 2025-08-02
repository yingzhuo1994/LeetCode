# 1st solution
# O(n * (n - k)) time | O(n - k) space
class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1:
            return s
        n = len(s)
        return max(s[i: i + n - k + 1] for i in range(n))


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def answerString(self, s: str, numFriends: int) -> str:
        if numFriends == 1:
            return s
        n = len(s)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        return s[i: i + n - numFriends + 1]