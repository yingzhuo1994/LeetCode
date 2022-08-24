# 1st solution
# O(n) time | O(log(n)) space
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        threeArray = []
        k = 0
        while 3**k <= n:
            threeArray.append(3**k)
            k += 1
        threeArray.reverse()

        def dfs(idx, left):
            if left == 0:
                return True
            if idx >= len(threeArray):
                return False
            num = threeArray[idx]
            if left > num:
                if dfs(idx + 1, left - num):
                    return True
            elif left == num:
                return True
            if dfs(idx + 1, left):
                return True
            return False
        
        return dfs(0, n)

# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 3)
            if r == 2: return False
        return True