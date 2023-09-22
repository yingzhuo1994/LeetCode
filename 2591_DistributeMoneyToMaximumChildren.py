# 1st solution
# O(1) time | O(1) space
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > 8 * children:
            return children - 1
        elif money == 8 * children:
            return children
        else:
            a, r = divmod(money - children, 7)
            if r == 0:
                return a
            elif r == 3:
                return min(a, children - 2)
            else:
                return min(a, children - 1)