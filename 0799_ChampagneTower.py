# 1st solution
# O(n^2) time | O(n^2) space 
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        stack = [[0 for _  in range(row + 1)] for row in range(query_row + 2)]
        stack[0][0] = poured
        for i in range(query_row + 1):
            isLeft = False
            for j in range(i + 1):
                if stack[i][j] > 1:
                    volumn = stack[i][j] - 1
                    isLeft = True
                    stack[i][j] = 1
                    stack[i+1][j] += volumn / 2
                    stack[i+1][j+1] += volumn / 2
            if not isLeft:
                break
        return stack[query_row][query_glass]

# 2nd solution
# O(n^2) time | O(n) space 
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        stack = [poured]
        for i in range(query_row + 1):
            isLeft = False
            nextStack = [0] * (i + 2)
            for j in range(i + 1):
                if stack[j] > 1:
                    volumn = stack[j] - 1
                    isLeft = True
                    stack[j] = 1
                    nextStack[j] += volumn / 2
                    nextStack[j+1] += volumn / 2
            if i != query_row:
                stack = nextStack
            if not isLeft:
                break
        return stack[query_glass] if query_glass < len(stack) else 0