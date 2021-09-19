class Solution:
    # 1st solution
    # O(n * n^4) time | O(n * n^4) space
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


    # 2nd solution
    # O(n * n^4) time | O(n * n^4) space
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return answers

    # 3rd solution
    # O(n * n^4) time | O(n * n^4) space
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        path = ''
        self.dfs(num, target, 0, path, 0, None, res)
        return res
    
    def dfs(self, num, target, idx, path, value, last, res):
        if idx == len(num) and value == target:
            res.append(path)
            return
        
        for i in range(idx + 1, len(num) + 1):
            tmp = int(num[idx:i])
            if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                if last is None:
                    self.dfs(num, target, i, num[idx: i], tmp, tmp, res)
                else:
                    self.dfs(num, target, i, path + "+" + num[idx: i], value + tmp, tmp, res)
                    self.dfs(num, target, i, path + "-" + num[idx: i], value - tmp, -tmp, res)
                    self.dfs(num, target, i, path + "*" + num[idx: i], value - last + last * tmp, last * tmp, res)
 