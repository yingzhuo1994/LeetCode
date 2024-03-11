# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDic = {ch: i for i, ch in enumerate(order)}
        lst = list(s)
        lst.sort(key=lambda v: [orderDic.get(v, 100), v])
        return "".join(lst)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        lst = []
        for ch in order:
            if ch in counts:
                lst.append(ch * counts[ch])
        for ch in counts:
            if ch not in order:
                lst.append(ch * counts[ch])
        return "".join(lst)