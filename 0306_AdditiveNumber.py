# 1st solution
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def isValid(a, b, c):
            first = int(num[a:b])
            second = int(num[b:c])
            third = first + second
            third_str = str(third)
            d = c + len(third_str)
            if n - c < len(third_str):
                return False
            elif num[c:d] != third_str:
                return False
            else:
                return d == n or isValid(b, c, d)
        a = 0
        if num[0] == "0":
            b = 1
            if num[b] == "0":
                c = b + 1
                if isValid(a, b, c):
                    return True
            else:
                for c in range(b + 1, n):
                    if isValid(a, b, c):
                        return True
        else:
            for b in range(a + 1, n - 1):
                if num[b] == "0":
                    c = b + 1
                    if isValid(a, b, c):
                        return True
                else:
                    for c in range(b + 1, n):
                        if isValid(a, b, c):
                            return True
        return False

# 2nd solution
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def isValid(a, b, c):
            first = int(num[a:b])
            second = int(num[b:c])
            third = first + second
            third_str = str(third)
            d = c + len(third_str)
            if n - c < len(third_str):
                return False
            elif num[c:d] != third_str:
                return False
            else:
                return d == n or isValid(b, c, d)
        a = 0
        for b in range(a + 1, n - 1):
            if num[:b] != str(int(num[:b])):
                break
            for c in range(b + 1, n):
                if num[b:c] != str(int(num[b:c])):
                    break
                if isValid(a, b, c):
                    return True
        return False