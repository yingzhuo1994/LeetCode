# 1st solution
# O(zero * one) time | O(zero * one) space
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if k == 0:
                return (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - (dfs(i - limit - 1, j, 1) if i > limit else 0)) % MOD
            else:  # else 可以去掉，这里仅仅是为了代码对齐
                return (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - (dfs(i, j - limit - 1, 0) if j > limit else 0)) % MOD
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        dfs.cache_clear()  # 防止爆内存
        return ans

# 2nd solution
# O(zero * one) time | O(zero * one) space
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        f = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(1, min(limit, zero) + 1):
            f[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            f[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                f[i][j][0] = (f[i - 1][j][0] + f[i - 1][j][1] - (f[i - limit - 1][j][1] if i > limit else 0)) % MOD
                f[i][j][1] = (f[i][j - 1][0] + f[i][j - 1][1] - (f[i][j - limit - 1][0] if j > limit else 0)) % MOD
        return sum(f[-1][-1]) % MOD

# 3rd solution
# O(zero * one / limit) time | O(min(zero, one))
MOD = 1_000_000_007
MX = 1001

fac = [0] * MX  # f[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

def comb(n: int, m: int) -> int:
    return fac[n] * inv_f[m] * inv_f[n - m] % MOD

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        if zero > one:
            zero, one = one, zero  # 保证空间复杂度为 O(min(zero, one))
        f0 = [0] * (zero + 3)
        for i in range((zero - 1) // limit + 1, zero + 1):
            f0[i] = comb(zero - 1, i - 1)
            for j in range(1, (zero - i) // limit + 1):
                f0[i] = (f0[i] + (-1 if j % 2 else 1) * comb(i, j) * comb(zero - j * limit - 1, i - 1)) % MOD

        ans = 0
        for i in range((one - 1) // limit + 1, min(one, zero + 1) + 1):
            f1 = comb(one - 1, i - 1)
            for j in range(1, (one - i) // limit + 1):
                f1 = (f1 + (-1 if j % 2 else 1) * comb(i, j) * comb(one - j * limit - 1, i - 1)) % MOD
            ans = (ans + (f0[i - 1] + f0[i] * 2 + f0[i + 1]) * f1) % MOD
        return ans