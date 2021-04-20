class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1st iterative solution
        # O(n) time | O(1) space
        n = len(digits)
        carry = 1
        i = 1
        while i <= n and carry > 0:
            if digits[-i] < 9:
                digits[-i] += carry
                carry = 0
            else:
                if carry == 1:
                    digits[-i] = 0
            i += 1
        if carry == 1:
            return [1] + digits
        else:
            return digits

        # 2nd recrusive solution
        # O(n) time | O(n) space
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] < 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return digits
