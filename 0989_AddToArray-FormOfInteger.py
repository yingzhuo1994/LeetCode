# 1st solution
# O(n) time | O(n) space
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        val = 0
        for i in range(len(num)):
            val += num[i] * pow(10, i)
        val += k
        ans = list(str(val))

        return [int(v) for v in ans]

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in reversed(range(len(num))):
            k, num[i] = divmod(num[i] + k, 10)
        return [int(i) for i in str(k)] + num if k > 0 else num