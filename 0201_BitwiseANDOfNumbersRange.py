class Solution:
    # 1st brute force solution
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        leftDigit = set([i for i in range(32)])
        for num in range(left, right + 1):
            if len(leftDigit) == 0:
                break
            bitPlace = [i for i in leftDigit]
            for kbit in bitPlace:
                if (num >> kbit) & 1:
                    continue
                else:
                    leftDigit.remove(kbit)
        result = 0
        for kbit in leftDigit:
            result = result | (1 << kbit)
        return result

    # 2nd solution
    # O(1) time | O(1) space
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        k = 0
        while left != right:
            left >>= 1
            right >>= 1
            k += 1
        return left << k