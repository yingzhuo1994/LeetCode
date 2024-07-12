# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def process(t, sub, score):
            stack = []
            value = 0
            for ch in t:
                stack.append(ch)
                if len(stack) >= 2 and stack[-2:] == sub:
                    stack.pop()
                    stack.pop()
                    value += score
            return stack, value

        first = ["a", "b"]
        second = ["b", "a"]
        if y > x:
            first, second = second, first
            x, y = y, x
        
        stack1, val1 = process(s, first, x)
        stack2, val2 = process(stack1, second, y)
        ans = val1 + val2

        return ans