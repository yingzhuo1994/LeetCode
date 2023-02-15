# 1st solution
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        val = 0
        for i in range(len(num)):
            val += num[i] * pow(10, i)
        val += k
        ans = list(str(val))

        return [int(v) for v in ans]