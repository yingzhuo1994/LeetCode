# 1st solution
# # O(kn) time | O(n) space 
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        lst = [ord(ch) - ord("a") + 1 for ch in s]
        num = "".join(map(str, lst))
        for _ in range(k):
            if len(num) == 1:
                break
            num = str(sum(map(int, list(num))))
        return int(num)
