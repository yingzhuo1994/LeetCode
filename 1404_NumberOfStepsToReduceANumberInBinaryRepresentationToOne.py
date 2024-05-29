# 1st solution
# O(n) time | O(n) space
class Solution:
    def numSteps(self, s: str) -> int:
        lst = list(s)[::-1]
        num = sum(int(lst[i]) * pow(2, i) for i in range(len(lst)))
        step = 0
        while num > 1:
            step += 1
            if num & 1:
                num += 1
            else:
                num >>= 1
        return step

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):  # Except first digit
            if int(s[i]) + carry == 1:  # Odd number
                carry = 1
                ans += 2  # 2 operations: Add 1 and divide by two
            else:
                ans += 1  # 1 operation: Divide by 2
        return ans + carry