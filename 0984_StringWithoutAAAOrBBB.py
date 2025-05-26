# 1st solution
# O(n) time | O(n) space
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ch1 = "a"
        ch2 = "b"
        if a < b:
            a, b = b, a
            ch1, ch2 = ch2, ch1

        q1, r1 = divmod(a, 2)
        q2, r2 = divmod(b, 2)
        s1 = [ch1 + ch1 for _ in range(q1)]
        if r1:
            s1 += [ch1 * r1]
        s2 = [ch2 + ch2 for _ in range(q2)]
        if r2:
            s2 += [ch2 * r2]
        while len(s1) - len(s2) > 1:
            if len(s2[0]) > 1:
                s2.pop(0)
                s2.append(ch2)
                s2.append(ch2)
            else:
                break

        s = []
        for i in range(len(s2)):
            s.append(s1[i])
            s.append(s2[i])
        if i + 1 < len(s1):
            s.append(s1[i + 1])
        return "".join(s)