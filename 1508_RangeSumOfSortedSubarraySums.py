# 1st solution
# O(n^2 * log(n)) time | O(n) space
from itertools import accumulate
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        prefix_sum = list(accumulate(nums)) + [0]
        array = []
        for i in range(n):
            for j in range(i, n):
                array.append(prefix_sum[j] - prefix_sum[i - 1])
        array.sort()
        ans = sum(array[left-1:right]) % MOD
        return ans

# 2nd solution
# O(n * log(S)) time | O(n) space
# S = sum(nums)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MODULO = 10**9 + 7
        prefixSums = [0]
        for i in range(n):
            prefixSums.append(prefixSums[-1] + nums[i])
        
        prefixPrefixSums = [0]
        for i in range(n):
            prefixPrefixSums.append(prefixPrefixSums[-1] + prefixSums[i + 1])

        def getCount(x: int) -> int:
            count = 0
            j = 1
            # 遍历虚拟矩阵的每一层，统计满足条件的个数
            for i in range(n):
	            # i 在不断增长，所以 prefixSums[i] 一直表示都是当前层的第一个元素
                while j <= n and prefixSums[j] - prefixSums[i] <= x:
	                # 符合条件就右移
                    j += 1
                j -= 1
                count += j - i
            return count

        def getKth(k: int) -> int:
	        # 这里整个二分查找就是求左边界
			# 即找到第一个满足 count == k 的值（使count == k的最小值）
            left, right = 0, prefixSums[n]
            while left <= right:
                mid = (left + right) // 2
                count = getCount(mid)
                if count < k:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def getSum(k: int) -> int:
            num = getKth(k)
            total, count = 0, 0
            j = 1
            # 遍历“虚拟矩阵”的每一层
            for i in range(n):
                while j <= n and prefixSums[j] - prefixSums[i] < num:
                    j += 1
                # 当前 j 位置的元素是 i 行 第 1 个大于等于 num 的值
                # 我们要找的是最后一个小于 num 的元素，所以 -1
                # 确定区间的右边界 j
                j -= 1

                # 计算区间和
                total += prefixPrefixSums[j] - prefixPrefixSums[i] - prefixSums[i] * (j - i)
                # 记录当前行符合条件的个数
                count += j - i
	        # 最后补上等于 num 的部分
            total += num * (k - count)
            return total

        return (getSum(right) - getSum(left - 1)) % MODULO