class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        num1 = list(num1)
        num1.reverse()
        num2 = list(num2)
        num2.reverse()
        ans = []
        i = 0
        carry = 0
        n1, n2 = len(num1), len(num2) 
        while i < n1 or i < n2 or carry > 0:
            a = int(num1[i]) if i < n1 else 0
            b = int(num2[i]) if i < n2 else 0
            val = a + b + carry
            carry = val // 10
            res = val % 10
            ans.append(str(res))
            i += 1
        ans.reverse()
        ans = "".join(ans)
        return ans