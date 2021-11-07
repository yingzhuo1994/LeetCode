class Solution:
    # 1st solution
    # O(mn) time | O(m + n) space
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        tenbit = 0
        for i in reversed(range(len(num2))):
            num = int(num2[i])
            curResult = self.multification(num, num1)
            for i in range(tenbit):
                curResult.append(0)
            self.addition(result, curResult[::-1])
            tenbit += 1 
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return "".join([str(result[i]) for i in reversed(range(len(result)))])
    
    def multification(self, num, s):
        result = [0] * (len(s) + 1)
        last = 0
        for i in reversed(range(len(s))):
            cur = num * int(s[i]) + last
            q = cur // 10
            r = cur % 10
            result[i + 1] = r
            last = q
        result[0] = last
        if last == 0:
            return result[1:]
        else:
            return result
        
    def addition(self, result, curResult):
        r = 0
        last = 0
        i = 0
        while i < len(result):
            a = curResult[i] if i < len(curResult) else 0
            b = result[i]
            curSum = a + b
            if curSum + last >= 10:
                r = 1
                curSum -= 10
            else:
                r = 0
            result[i] = curSum + last
            last = r
            i += 1
            
