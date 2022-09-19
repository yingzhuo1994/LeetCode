# O(n) time | O(n) space
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        lines = []

        i = 0
        while i < n:
            line = []
            length = -1
            j = i
            while j < n:
                word = words[j]
                if length + 1 + len(word) <= maxWidth:
                    length += 1 + len(word)
                    line.append(word)
                    j += 1
                else:
                    break
            lines.append(line)
            i = j
        
        ans = []
        m = len(lines)
        for i in range(m - 1):
            line = lines[i]
            k = len(line)
            if k == 1:
                ans.append(line[0] + " " * (maxWidth - len(line[0])))
                continue
            totalLength = maxWidth
            for word in line:
                totalLength -= len(word)
            q, r = divmod(totalLength, k - 1)
            splitLength = [q] * (k - 1) + [0]
            for j in range(r):
                splitLength[j] += 1
            stack = []
            for j in range(k):
                stack.append(line[j])
                stack.append(" " * splitLength[j])
            ans.append("".join(stack))
        line = lines[-1]
        lastLine = " ".join(line)
        leftLength = maxWidth - len(lastLine)
        lastLine += " " * leftLength
        ans.append(lastLine)

        return ans