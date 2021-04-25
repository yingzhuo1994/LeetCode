class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right):
            if left > right or left < 0:
                return []
            elif left == right:
                return ['(' + paren for paren in helper(left - 1, right)]
            elif right == 1:
                return [')']
            lst = []
            addLeft = ["(" + paren for paren in helper(left - 1, right)]
            addRight = [")" + paren for paren in helper(left, right - 1)]
            return addLeft + addRight
        return helper(n, n)
