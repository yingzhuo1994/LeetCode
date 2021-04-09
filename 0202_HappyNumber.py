class Solution:
    def isHappy(self, n: int) -> bool:
        dic = []
        while True:
            if n == 1:
                return True
            if n not in dic:
                dic.append(n)
                newN = 0
                for num in str(n):
                    newN += int(num) * int(num)
                n = newN
            else:
                return False
        return False
