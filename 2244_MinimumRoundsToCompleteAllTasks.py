# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)
        for v in count.values():
            if v < 2:
                return -1
        def cal(n):
            if n % 3 == 0:
                return n // 3
            else:
                return n // 3 + 1
        ans = 0
        for val in count.values():
            ans += cal(val)
        return ans