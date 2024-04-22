# 1st solution
# O(n) time | O(n) space
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        for k, v in cnt.items():
            q, r = divmod(v, k + 1)
            if r > 0:
                q += 1
            ans += q * (k + 1)
        return ans