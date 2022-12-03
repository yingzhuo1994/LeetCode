# 1st solution
# O(1） time | O(1) space
class Solution:
    def toHex(self, num: int) -> str:
        dic = {i: str(i) for i in range(10)}
        for i in range(10, 16):
            dic[i] = chr(ord("a") + i - 10)
        
        if num >= 0:
            ans = []
            while num > 0:
                num, r = divmod(num, 16)
                ans.append(dic[r])
            if not ans:
                ans.append("0")
            ans.reverse()
            return "".join(ans)
        else:
            MAX = 0
            for k in range(8):
                MAX += 15 * 16**k
            return self.toHex(MAX + 1 + num)