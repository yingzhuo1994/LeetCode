# 1st solution
# O(n) time | O(n) space
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def helper(start, end):
            if expression[start] == "!":
                return not helper(start + 2, end - 1)
            elif expression[start] in "&|":
                op = expression[start]
                i = start + 2
                start = i
                while i <= end:
                    if expression[i] in "!&|":
                        j = i + 2
                        left = 1
                        while left > 0:
                            if expression[j] == "(":
                                left += 1
                            elif expression[j] == ")":
                                left -= 1
                            j += 1
                        if op == "&":
                            if not helper(i, j - 1):
                                return False
                        else:
                            if helper(i, j - 1):
                                return True
                        i = j
                    elif expression[i] == "," or i == end:
                        if op == "&":
                            if not helper(start, i - 1):
                                return False
                        else:
                            if helper(start, i - 1):
                                return True
                        start = i + 1
                        i += 1
                    else:
                        i += 1
                if op == "&":
                    return True
                else:
                    return False
            elif expression[start] == "t":
                return True
            else:
                return False
            
        
        return helper(0, len(expression) - 1)


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        def calc(a, b, op):
            x, y = a == 't', b == 't'
            ans = x | y if op == '|' else x & y
            return 't' if ans else 'f'
        nums, ops = [], []
        for c in s:
            if c == ',':
                continue
            if c == 't' or c == 'f':
                nums.append(c)
            if c == '|' or c == '&' or c == '!':
                ops.append(c)
            if c == '(':
                nums.append('-')
            if c == ')':
                op, cur = ops.pop(), ' '
                while nums and nums[-1] != '-':
                    top = nums.pop()
                    cur = top if cur == ' ' else calc(cur, top, op)
                if op == '!':
                    cur = 't' if cur == 'f' else 'f'
                nums.pop()
                nums.append(cur)
        return nums[-1] == 't'