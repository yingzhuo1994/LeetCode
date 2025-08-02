# 1st solution
# O((n/k)! * n) time | O(n) space
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        s = [ord(c) - ord('a') for c in s]  # 转成 0 到 25，这样下面无需频繁调用 ord

        # 392. 判断子序列（进阶做法）
        n = len(s)
        nxt = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            nxt[i][:] = nxt[i + 1]
            nxt[i][s[i]] = i

        def isSubsequence(seq: Tuple[int, ...]) -> bool:
            i = -1
            for _ in range(k):
                for c in seq:
                    i = nxt[i + 1][c]
                    if i == n:  # c 不在 s 中，说明 seq*k 不是 s 的子序列
                        return False
            return True  # seq*k 是 s 的子序列

        cnt = Counter(s)
        a = [ch for ch, freq in cnt.items() for _ in range(freq // k)]
        a.sort(reverse=True)  # 排序后，下面会按照字典序从大到小枚举排列

        for i in range(len(a), 0, -1):  # 长度优先
            for seq in permutations(a, i):  # 枚举 a 的长为 i 的排列
                if isSubsequence(seq):
                    return ''.join(ascii_lowercase[c] for c in seq)
        return ''