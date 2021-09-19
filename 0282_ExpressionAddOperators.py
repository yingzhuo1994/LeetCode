class Solution:
    # 1st solution
    # O(n^4) time | O(n) space
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        path = ''
        self.dfs(num, target, 0, path, res)
        return res
    
    def dfs(self, num, target, idx, path, res):
        if idx >= len(num):
            if self.checkResult(target, path):
                res.append(path)
            return 
        self.dfs(num, target, idx + 1, path + num[idx], res)
        if len(path) > 0:
            for operator in '+-*':
                self.dfs(num, target, idx + 1, path + operator + num[idx], res)

    def checkResult(self, target, path):
        stack = []
        num = 0
        operator = '+'
        start = 0
        for i, ch in enumerate(path):
            if ch.isdigit():
                if i > start and path[start] == '0':
                    return False
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(path) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack[-1] *= num
                num = 0
                start = i + 1
                operator = ch

        return target == sum(stack)