# 1st solution
# O(n) time | O(n) space
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        index = [0, 0, 0]
        vals = [1, 1, 1]
        ans = [1]
        last = 1
        k = 3
        while len(ans) < n:
            for i in range(k):
                if vals[i] == last:
                    vals[i] = ans[index[i]] * primes[i]
                    index[i] += 1
            last = min(vals)
            ans.append(last)
        return last


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ans 用作存储已有丑数（从下标 1 开始存储，第一个丑数为 1）
        ans = [0] * (n + 1)
        ans[1] = 1
        # 由于三个有序序列都是由「已有丑数」*「质因数」而来
        # i2、i3 和 i5 分别代表三个有序序列当前使用到哪一位「已有丑数」下标（起始都指向 1）
        i2 = i3 = i5 = 1
        idx = 2
        while idx <= n:
            # 由 ans[iX] * X 可得当前有序序列指向哪一位
            a, b, c = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            # 将三个有序序列中的最小一位存入「已有丑数」序列，并将其下标后移
            m = min(a, b, c)
            # 由于可能不同有序序列之间产生相同丑数，因此只要一样的丑数就跳过（不能使用 else if ）
            if m == a:
                i2 += 1
            if m == b:
                i3 += 1
            if m == c:
                i5 += 1
            ans[idx] = m
            idx += 1
        return ans[n]