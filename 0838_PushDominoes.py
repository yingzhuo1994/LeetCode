# 1st solution
# O(n) time | O(n) space
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        stack = ["."] * len(dominoes)
        last = 0
        lastDirection = "0"
        for i, direction in enumerate(dominoes):
            length = i - last + 1
            if direction == "L":
                if lastDirection != "R":
                    stack[last:last+length] = ["L"] * length
                else:
                    half = length // 2
                    stack[last:last+half] = ["R"] * half
                    stack[i+1-half:i+1] = ["L"] * half
                last = i
                lastDirection = "L"
            elif direction == "R":
                if lastDirection == "R":
                    stack[last:last+length] = ["R"] * length
                last = i
                lastDirection = "R"
            # print(i, stack)
        if lastDirection == "R":
            stack[last:] = ["R"] * len(stack[last:])
        return "".join(stack)

