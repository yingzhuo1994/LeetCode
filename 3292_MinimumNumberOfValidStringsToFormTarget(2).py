# 1st solution
# O(L + nm) time | O(l + n) space
# where L is sum length of word in words, n = len(target), and m = len(words)
class Solution:
    def calc_z(self, s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        box_l = box_r = 0  # z-box 左右边界（闭区间）
        for i in range(1, n):
            if i <= box_r:
                z[i] = min(z[i - box_l], box_r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                box_l, box_r = i, i + z[i]
                z[i] += 1
        return z

    # 桥的概念，见我在 45 或 1326 题下的题解
    def jump(self, max_jumps: List[int]) -> int:
        ans = 0
        cur_r = 0  # 已建造的桥的右端点
        nxt_r = 0  # 下一座桥的右端点的最大值
        for i, max_jump in enumerate(max_jumps):  # 如果走到 n-1 时没有返回 -1，那么必然可以到达 n
            nxt_r = max(nxt_r, i + max_jump)
            if i == cur_r:  # 到达已建造的桥的右端点
                if i == nxt_r:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_r = nxt_r  # 造一座桥
                ans += 1
        return ans

    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        max_jumps = [0] * n
        for word in words:
            z = self.calc_z(word + "#" + target)
            m = len(word) + 1
            for i in range(n):
                max_jumps[i] = max(max_jumps[i], z[m + i])
        return self.jump(max_jumps)