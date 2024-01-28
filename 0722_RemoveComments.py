# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        t = []
        block_comment = False
        for line in source:
            i, m = 0, len(line)
            while i < m:
                if block_comment:
                    if i + 1 < m and line[i : i + 2] == "*/":
                        block_comment = False
                        i += 1
                else:
                    if i + 1 < m and line[i : i + 2] == "/*":
                        block_comment = True
                        i += 1
                    elif i + 1 < m and line[i : i + 2] == "//":
                        break
                    else:
                        t.append(line[i])
                i += 1
            if not block_comment and t:
                ans.append("".join(t))
                t.clear()
        return ans
