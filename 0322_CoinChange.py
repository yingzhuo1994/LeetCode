class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for _ in range(amount + 1)]
        table[0] = 0
        for denom in coins:
            for i in range(1, len(table)):
                if denom <= i:
                    table[i] = min(table[i], 1 + table[i - denom])
        return -1 if table[-1] == float('inf') else table[-1]