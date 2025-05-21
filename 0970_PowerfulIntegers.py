# 1st solution
# O(log(n) ^ 2) time | O(log(n) ^ 2) space
# where n = bound
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x > y:
            x, y = y, x
        ans = set()
        if y == 1:
            if 2 <= bound:
                return [2]
            return []
        elif x == 1:
            a = 1
            for j in range(0, bound + 1):
                b = pow(y, j)
                if a + b > bound:
                    break
                ans.add(a + b)
        
        for i in range(0, bound + 1):
            a = pow(x, i)
            if a > bound:
                break
            for j in range(0, bound + 1):
                b = pow(y, j)
                if a + b > bound:
                    break
                ans.add(a + b)
        return list(ans)