# 1st solution
# O(n^3 * log(n)) time | O(n^3) space
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and digits[k] % 2 == 0:
                        ans.add(num)
        return sorted(list(ans))