# 1st recursive solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right):
            if left > right or left < 0:
                return []
            if left == 0 and right == 1:
                return [')']
            addLeft = ["(" + paren for paren in helper(left - 1, right)]
            addRight = [")" + paren for paren in helper(left, right - 1)]
            return addLeft + addRight

        return helper(n, n)

# 2nd backtracking solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()

        ans = []
        backtrack()
        return ans