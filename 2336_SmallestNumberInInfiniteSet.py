# 1st solution
# O(n^2) time | O(n) space
class SmallestInfiniteSet:
    def __init__(self):
        self.numSet = set()

    def popSmallest(self) -> int:
        num = 1
        while num in self.numSet:
            num += 1
        self.numSet.add(num)
        return num

    def addBack(self, num: int) -> None:
        if num in self.numSet:
            self.numSet.remove(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
