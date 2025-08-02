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


# 2nd solution
# O(L + n) time | O(L + n) space
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # 多项式字符串哈希（方便计算子串哈希值）
        # 哈希函数 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

        # 计算子串 target[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
        # 计算方法类似前缀和
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

        # 保存每个 words[i] 的每个前缀的哈希值，按照长度分组
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        for w in words:
            h = 0
            for j, b in enumerate(w):
                h = (h * BASE + ord(b)) % MOD
                sets[j].add(h)  # 注意 j 从 0 开始

        ans = 0
        cur_r = 0  # 已建造的桥的右端点
        nxt_r = 0  # 下一座桥的右端点的最大值
        for i in range(n):
            while nxt_r < n and nxt_r - i < max_len and sub_hash(i, nxt_r + 1) in sets[nxt_r - i]:
                nxt_r += 1  # 尽量伸长
            if i == cur_r:  # 到达已建造的桥的右端点
                if i == nxt_r:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_r = nxt_r  # 建造下一座桥
                ans += 1
        return ans