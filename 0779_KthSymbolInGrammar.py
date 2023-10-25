# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def g(num, i):
            if num == 0:
                stack = [0, 1]
            else:
                stack = [1, 0]
            return stack[i]
        
        if n == 1:
            return 0
        
        q, r = divmod(k + 1, 2)
        return g(self.kthGrammar(n - 1, q), r)
    