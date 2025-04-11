# 1st solution
# O(n) time | O(1) space
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num = low
        ans = 0
        while num <= high:
            if len(str(num)) & 1:
                num = pow(10, len(str(num)))
                continue
            front = 0
            s = str(num)
            for i in range(len(s) // 2):
                front += int(s[i])
            back = 0
            for i in range(len(s) // 2, len(s)):
                back += int(s[i])
            ans += front == back
            num += 1
        return ans