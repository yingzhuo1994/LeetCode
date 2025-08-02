# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def weight(x):
            if x != 1:
                if x & 1:
                    x = 3 * x + 1
                else:
                    x = x // 2
                return 1 + weight(x)
            return 0
            
        lst = list(range(lo, hi + 1))
        lst.sort(key=lambda v: [weight(v), v])
        return lst[k - 1]