# 1st solution
class ATM:
    def __init__(self):
        self.money = {20: 0, 50: 0, 100: 0, 200:0, 500:0}   
        self.moneyOrder = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, value in enumerate(self.moneyOrder):
            self.money[value] += banknotesCount[i]


    def withdraw(self, amount: int) -> List[int]:
        ans = [0, 0, 0, 0, 0]
        for i in reversed(range(len(self.moneyOrder))):
            value = self.moneyOrder[i]
            if amount >= value and self.money[value] > 0:
                cnt = amount // value
                ans[i] = min(cnt, self.money[value])
                amount -= ans[i] * value
        if amount != 0:
            return [-1]
        for i, value in enumerate(self.moneyOrder):
            self.money[value] -= ans[i]
        return ans

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)