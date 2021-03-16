class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic ={'(': ')', '[': ']', '{': '}'}
        n = len(s)
        # if n == 2:
        #     if s[0] in dic and dic[s[0]] == s[1]:
        #         return True
        #     else:
        #         return False
        if n % 2 == 1:
            return False
        # for i in range(n):
        #     if s[i] not in dic:
        #         if i == 0 or dic[s[i-1]] != s[i]:
        #             return False
        #         else:
        #             return self.isValid(s[:i - 1] + s[i + 1:])

        stack = []
        for paren in s:
            if paren in dic:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if dic[last_open] != paren:
                    return False
        return len(stack) == 0
