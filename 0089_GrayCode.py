# 1st solution, TLE
# O(2^n) time | O(n) space
class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst = [0]
        visited = set([0])
        def dfs(lst, visited):
            if len(lst) == 2**n:
                d = lst[-1]
                one = ((d - 1) & d) ^ d
                if d ^ one == 0:
                    return True
                else:
                    return False
            
            addOneLst = self.addOne(lst[-1], n)
            removeOneLst = self.removeOne(lst[-1])
            if len(lst) == 1 or lst[-1] > lst[-2]:
                candidates = addOneLst + removeOneLst
            else:
                candidates = removeOneLst + addOneLst
            for num in candidates:
                if num in visited:
                    continue
                lst.append(num)
                visited.add(num)
                if dfs(lst, visited):
                    return True
                lst.pop()
                visited.remove(num)
            return False
        dfs(lst, visited)
        return lst
            
    def addOne(self, num, n):
        lst = []
        for i in range(n + 1):
            if not ((1 << i) & num):
                d = num | (1 << i)
                if d < 2**n:
                    lst.append(d)
        return lst
    
    def removeOne(self, num):
        d = num
        lst = []
        while d > 0:
            last = ((d - 1) & d) ^ d
            lst.append(num ^ last)
            d ^= last
        return lst