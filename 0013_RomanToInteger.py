class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # def substitute(c):
            # if c == 'I':
            #     return 1
            # elif c == 'V':
            #     return 5
            # elif c == 'X':
            #     return 10
            # elif c == 'L':
            #     return 50
            # elif c == 'C':
            #     return 100
            # elif c == 'D':
            #     return 500
            # elif c == 'M':
            #     return 1000
            # else:
            #     return None

        # def transfrom(t):
        #     num = 0
        #     if len(t) == 1:
        #         return t[0]
        #     for i in range(len(t) - 1):
        #         if t[i] >= t[i+1]:
        #             num += t[i]
        #         else:
        #             num -= t[i]
        #     num += t[-1]
        #     return num

        # lst = [0 for _ in range(len(s))]
        # for i in range(len(s)):
        #     lst[i] = substitute(s[i])
        # return transfrom(lst)

        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        for i in range(len(s) - 1):
            if dic[s[i]] >= dic[s[i + 1]]:
                num += dic[s[i]]
            else:
                num -= dic[s[i]]
        num += dic[s[-1]]
        return num
