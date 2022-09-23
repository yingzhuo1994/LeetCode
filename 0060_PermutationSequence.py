# 1st solution
# O(n^2) time | O(n) space
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]
        ans = []
        def permutationWithK(lst, ans, k):
            length = len(lst)
            if length == 0:
                return
            m = math.factorial(length - 1)
            i = (k - 1) // m
            r = (k - 1) % m + 1
            ans.append(lst.pop(i))
            permutationWithK(lst, ans, r)
        
        permutationWithK(lst, ans, k)
        return "".join(ans)