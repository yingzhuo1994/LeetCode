# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        n = len(baskets)
        used = [False] * n
        for fruit in fruits:
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = 1
                    cnt += 1
                    break
        return n - cnt