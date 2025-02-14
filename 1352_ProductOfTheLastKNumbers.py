# 1st solution
# O(n) time | O(n) space
class ProductOfNumbers:

    def __init__(self):
        self.array = [1]
        self.zeros = [0]
        self.product = [1]

    def add(self, num: int) -> None:
        self.array.append(num)
        if num == 0:
            self.zeros.append(self.zeros[-1] + 1)
            self.product.append(self.product[-1])
        else:
            self.zeros.append(self.zeros[-1])
            self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        zero = self.zeros[-1] - self.zeros[-k-1]
        if zero > 0:
            return 0
        return self.product[-1] // self.product[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)