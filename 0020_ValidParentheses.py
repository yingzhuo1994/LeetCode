class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic ={'(': ')', '[': ']', '{': '}'}
        n = len(s)

        if n % 2 == 1:
            return False

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
