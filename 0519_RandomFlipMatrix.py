import random
class Solution:
    def __init__(self, m: int, n: int):
        self.c = n
        self.end = m * n - 1
        self.dic = {}
        self.start = 0

    def flip(self) -> List[int]:
        rand = random.randint(self.start, self.end)
        res = self.dic.get(rand, rand)
        self.dic[rand] = self.dic.get(self.start, self.start)
        self.start += 1
        return divmod(res, self.c)

    def reset(self) -> None:
        self.dic = {}
        self.start = 0

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()