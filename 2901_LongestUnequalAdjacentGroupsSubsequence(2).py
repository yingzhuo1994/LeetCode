# 1st solution
# O(n) time | O(n) space
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        f_map = {}  # 哈希值 -> (max_f, j, max_f2, j2)
        from_ = [0] * n
        global_max_f = max_i = 0
        for i in range(n - 1, -1, -1):
            w, g = words[i], groups[i]

            # 计算 w 的哈希值
            hash_val = sum((ord(ch) & 31) << (k * 5) for k, ch in enumerate(w))

            f = 0  # 方法一中的 f[i]
            for k in range(len(w)):
                h = hash_val | (31 << (k * 5))  # 用记号笔把 w[k] 涂黑（置为 11111）
                max_f, j, max_f2, j2 = f_map.get(h, (0, 0, 0, 0))
                if g != groups[j]:  # 可以从最大值转移过来
                    if max_f > f:
                        f = max_f
                        from_[i] = j
                else:  # 只能从次大值转移过来
                    if max_f2 > f:
                        f = max_f2
                        from_[i] = j2

            f += 1
            if f > global_max_f:
                global_max_f, max_i = f, i

            # 用 f 更新 f_map[h] 的最大次大
            # 注意要保证最大次大的 group 值不同
            for k in range(len(w)):
                h = hash_val | (31 << (k * 5))
                max_f, j, max_f2, j2 = f_map.get(h, (0, 0, 0, 0))
                if f > max_f:  # 最大值需要更新
                    if g != groups[j]:
                        max_f2, j2 = max_f, j  # 旧最大值变成次大值
                    max_f, j = f, i
                elif f > max_f2 and g != groups[j]:  # 次大值需要更新
                    max_f2, j2 = f, i
                f_map[h] = (max_f, j, max_f2, j2)

        ans = [''] * global_max_f
        i = max_i
        for k in range(global_max_f):
            ans[k] = words[i]
            i = from_[i]
        return ans
