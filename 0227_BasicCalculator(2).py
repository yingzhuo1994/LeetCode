class Solution:
    def calculate(self, s: str) -> int:
        # 1st solution
        # O(n) time | O(n) space
        lst = []
        for i in range(len(s)):
            if s[i] in '+-*/':
                lst.append(s[i])
            elif s[i].isalnum():
                if lst and lst[-1].isalnum():
                    lst[-1] += s[i]
                else:
                    lst.append(s[i])

        i = 0
        while i < len(lst):
            if lst[i].isalnum() or lst[i] in '+-':
                i += 1
                continue
            if lst[i] == '*':
                result = int(lst[i-1]) * int(lst[i+1])
            elif lst[i] == '/':
                result = int(int(lst[i-1]) / int(lst[i+1]))
            lst.pop(i+1)
            lst.pop(i)
            lst[i-1] = str(result)
        
        i = 0
        while i < len(lst):
            if lst[i].isalnum():
                i += 1
                continue
            if lst[i] == '+':
                result = int(lst[i-1]) + int(lst[i+1])
            elif lst[i] == '-':
                result = int(lst[i-1]) - int(lst[i+1])
            lst.pop(i+1)
            lst.pop(i)
            lst[i-1] = str(result)
        return int(lst[0])      