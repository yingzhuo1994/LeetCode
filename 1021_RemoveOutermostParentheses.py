class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        start = 0
        cnt = 0
        for i, ch in enumerate(s):
            if ch == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans.append(s[start+1:i])
                start = i + 1
        return "".join(ans)