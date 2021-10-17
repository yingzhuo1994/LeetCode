class Solution:
    # 1st solution, Lagrange's four square theorem
    # O(sqart(n)) time | O(1) space
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3

    # 2nd solution
    # O(n^2) time | O(n^2) space
    def numSquares(self, n: int) -> int:
        squareSet = set()
        k = 1
        while k * k <= n:
            squareSet.add(k * k)
            k += 1
        
        count = 0
        stack = set([n])
        while stack:
            count += 1
            newStack = set()
            for val in stack:
                for sq in squareSet:
                    if sq < val:
                        newStack.add(val - sq)
                    elif sq == val:
                        return count
            stack = newStack