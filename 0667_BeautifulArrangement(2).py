# 1st solution
# O(n) time | O(n) space
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = [i for i in range(1, n + 1)]
        sign = 1
        for i in range(1, k + 1):
            diff = k + 1 - i
            answer[i] = answer[i - 1] + sign * diff
            sign *= -1
        return answer