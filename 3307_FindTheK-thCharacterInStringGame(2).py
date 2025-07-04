# 1st solution
# O(log(k)) time | O(1) space
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if not operations:
            return 'a'
        op = operations.pop()
        # 注意 pop 之后 operations 的长度减少了 1，所以下面写的是 1<<n 而不是 1<<(n-1)
        m = 1 << len(operations)
        if k <= m:  # k 在左半边
            return self.kthCharacter(k, operations)
        # k 在右半边
        ans = self.kthCharacter(k - m, operations)
        return ascii_lowercase[(ord(ans) - ord('a') + op) % 26]

