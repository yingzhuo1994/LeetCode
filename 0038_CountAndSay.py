class Solution:
    def countAndSay(self, n: int) -> str:
        # O(2^n) time | O(2^(n-1)) space
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        lst = []
        count = 0
        ch = s[0]
        for elem in s:
            if elem == ch:
                count += 1
            else:
                lst.append(str(count))
                lst.append(ch)
                ch = elem
                count = 1
        lst.append(str(count))
        lst.append(ch)
        return ''.join(lst)
