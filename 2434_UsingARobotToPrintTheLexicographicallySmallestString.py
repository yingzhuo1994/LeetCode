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


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def robotWithString(self, s: str) -> str:
      n = len(s)
      # 计算后缀最小值
      suf_min = ['z'] * (n + 1)
      for i in range(n - 1, -1, -1):
          suf_min[i] = min(suf_min[i + 1], s[i])

      ans = []
      st = []
      for i, ch in enumerate(s):
          st.append(ch)
          while st and st[-1] <= suf_min[i + 1]:
              ans.append(st.pop())
      return ''.join(ans)