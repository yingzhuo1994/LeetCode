class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = len(digits)
        # i = 1
        # carry = 1
        # while i <= n:
        #     if digits[-i] < 9:
        #         digits[-i] += carry
        #         return digits
        #     else:
        #         if carry == 1:
        #             digits[-i] = 0
        #         else:
        #             carry = 0
        #     i += 1
        # if carry == 1:
        #     return [1] + digits

        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits
