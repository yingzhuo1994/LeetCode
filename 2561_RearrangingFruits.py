# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1

        a = []
        for x, c in cnt.items():
            if c % 2:
                return -1
            a.extend([x] * (abs(c) // 2))

        a.sort()
        mn = min(cnt)

        return sum(min(x, mn * 2) for x in a[:len(a) // 2])