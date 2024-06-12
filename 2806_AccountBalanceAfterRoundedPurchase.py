# 1st solution
# O(1) time | O(1) space 
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        q, r = divmod(purchaseAmount, 10)
        if 10 - r <= r:
            return 100 - (q + 1) * 10
        else:
            return 100 - q * 10

# 2nd solution
# O(1) time | O(1) space 
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10