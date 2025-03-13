# 1st solution, TLE
# O(nq) time | O(1) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        zeros = sum(num == 0 for num in nums)
        n = len(nums)
        if zeros == n:
            return 0
        for i, query in enumerate(queries, 1):
            l, r, val = query
            for j in range(l, r + 1):
                if nums[j] > 0:
                    nums[j] = max(0, nums[j] - val)
                    if nums[j] == 0:
                        zeros += 1
            if zeros == n:
                return i
        return -1


# 2nd solution
# O((n + q) * log(q)) time | O(n) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # 3355. 零数组变换 I
        def check(k: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for l, r, val in queries[:k]:  # 前 k 个询问
                diff[l] += val
                diff[r + 1] -= val

            for x, sum_d in zip(nums, accumulate(diff)):
                if x > sum_d:
                    return False
            return True

        q = len(queries)
        left, right = -1, q + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if right <= q else -1