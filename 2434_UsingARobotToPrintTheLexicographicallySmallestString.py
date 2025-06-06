# 1st solution
# O(n) time | O(n) space
class Solution:
    def robotWithString(self, s: str) -> str:
        alpha = string.ascii_lowercase
        ans = []
        t = []
        front = Counter(s)
        back = Counter(s)
        i = 0
        while i < len(s):
            m = None
            for ch in alpha:
                if back[ch] > 0:
                    m = ch
                    break
            if m and t and t[-1] <= m:
                ans.append(t[-1])
                front[t[-1]] -= 1
                t.pop()
                continue
            t.append(s[i])
            front[t[-1]] += 1
            back[t[-1]] -= 1
            i += 1
        ans += t[::-1]
        return "".join(ans)
