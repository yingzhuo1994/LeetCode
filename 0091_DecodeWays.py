class Solution:
    def numDecodings(self, s: str) -> int:
        # 1st solution
        # O(n) time | O(n) space
        lst = [1 for _ in range(len(s) + 1)]
        if int(s[0]) > 0:
            lst[1] = 1
        else:
            return 0
        for i in range(2, len(s) + 1):
            single, double = 0, 0
            if int(s[i-1]) > 0:
                single = 1
            if 10 <= int(s[i-2:i]) <= 26:
                double = 1
            if single or double:
                lst[i] = lst[i-1] * single + lst[i-2] * double
            else:
                return 0
        return lst[-1] 

        # 2nd solution
        # O(n) time | O(1) space
        front = 1
        if int(s[0]) > 0:
            back = 1
        else:
            return 0
        for i in range(1, len(s)):
            single, double = 0, 0
            if int(s[i]) > 0:
                single = 1
            if 10 <= int(s[i-1:i+1]) <= 26:
                double = 1
            if single or double:
                cur = back * single + front * double
                front, back = back, cur
            else:
                return 0
        return back