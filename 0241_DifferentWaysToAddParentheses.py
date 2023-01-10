# 1st solution
# O(n!) time | O(n!) space
# where n is the number of operators
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        stack = []
        num = 0
        for i, ch in enumerate(expression):
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                stack.append(num)
                num = 0
                stack.append(ch)
        stack.append(num)
        memo = {}
        def dfs(stack):
            key = tuple(stack)
            if key in memo:
                return memo[key]
            memo[key] = []
            if len(stack) == 1:
                memo[key] = stack
                return memo[key]
            
            for i, ch in enumerate(stack):
                if type(ch) == str:
                    front = dfs(stack[:i])
                    back = dfs(stack[i+1:])
                    for a in front:
                        for b in back:
                            if ch == "+":
                                num = a + b
                            elif ch == "-":
                                num = a - b
                            else:
                                num = a * b
                            memo[key].append(num)
            return memo[key]

        return dfs(stack)