class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = 1
        carry = 1
        while i <= n:
            if digits[-i] < 9:
                digits[-i] += carry
                return digits
            else:
                if carry == 1:
                    digits[-i] = 0
                else:
                    carry = 0
            i += 1
        if carry == 1:
            return [1] + digits
