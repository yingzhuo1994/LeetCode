class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if c.isdigit() :
                num = int(c)
                if len(stack) == 0:
                    stack.append(num)
                elif len(stack) == 1:
                    if num > stack[0]:
                        stack.append(stack[0])
                        stack[0] = num
                    elif num < stack[0]:
                        stack.append(num)
                else:
                    if num > stack[0]:
                        stack[0], stack[1] = num, stack[0]
                    elif stack[0] > num > stack[1]:
                        stack[1] = num
        if len(stack) == 2:
            return stack[-1]
        return -1
