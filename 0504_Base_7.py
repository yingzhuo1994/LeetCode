# O(1) time | O(1) space
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return "-" + self.convertToBase7(-num)
        stack = []
        while num > 0:
            num, r = divmod(num, 7)
            stack.append(str(r))
        stack.reverse()
        return "".join(stack)