# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDic = {ch: i for i, ch in enumerate(order)}
        lst = list(s)
        lst.sort(key=lambda v: [orderDic.get(v, 100), v])
        return "".join(lst)