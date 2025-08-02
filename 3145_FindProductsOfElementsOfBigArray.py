# 1st solution, MLE
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def getBigNum(num):
            val = bisect.bisect_left(nums, num)
            i = num - nums[val - 1]
            for _ in range(i - 1):
                val &= val - 1
            val ^= val & (val - 1)
            # print(num, val)
            return val
        
        n = max(query[1] for query in queries)
        nums = [0]
        val = 1
        while nums[-1] < n:
            cnt = bin(val).count("1")
            nums.append(nums[-1] + cnt)
            val += 1
        # print(n, nums)
        ans = []
        for start, end, MOD in queries:
            product = 1
            for val in range(start, end + 1):
                product *= getBigNum(val + 1)
            product %= MOD
            ans.append(product)
        return ans

# 2nd solution
# O(q * log(r)) time | O(1) space
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def sum_e(k: int) -> int:
            res = n = cnt1 = sum_i = 0
            for i in range((k + 1).bit_length() - 1, 0, -1):
                c = (cnt1 << i) + (i << (i - 1))  # 新增的幂次个数
                if c <= k:
                    k -= c
                    res += (sum_i << i) + ((i * (i - 1) // 2) << (i - 1))
                    sum_i += i  # 之前填的 1 的幂次之和
                    cnt1 += 1  # 之前填的 1 的个数
                    n |= 1 << i  # 填 1
            # 最低位单独计算
            if cnt1 <= k:
                k -= cnt1
                res += sum_i
                n |= 1  # 最低位填 1
            # 剩余的 k 个幂次，由 n 的低 k 个 1 补充
            for _ in range(k):
                lb = n & -n
                res += lb.bit_length() - 1
                n ^= lb  # 去掉最低位的 1（置为 0）
            return res
        return [pow(2, sum_e(r + 1) - sum_e(l), mod) for l, r, mod in queries]