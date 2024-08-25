# 1st solution, TLE
# O(k*2^n) time | O(n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if len(nums) < k or total % k != 0:
            return False
        goal = total // k

        nums.sort(reverse=True)
        visited = [False] * len(nums)

        def can_partition(rest_k, cur_sum=0, next_index=0):
            if rest_k == 1:
                return True

            if cur_sum == goal:
                return can_partition(rest_k - 1)

            for i in range(next_index, len(nums)):
                if not visited[i] and cur_sum + nums[i] <= goal:
                    visited[i] = True
                    if can_partition(rest_k, cur_sum + nums[i], i + 1):
                        return True
                    visited[i] = False
            return False

        return can_partition(k)


# 2nd solution
# O(2^n*n) time | O(2^n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        nums.sort(reverse=True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket:
            return False

        dp = [-1] * (1 << N)
        dp[0] = 0
        for mask in range(1 << N):
            for j in range(N):
                neib = dp[mask ^ (1 << j)]
                if mask & (1 << j) and neib >= 0 and neib + nums[j] <= basket:
                    dp[mask] = (neib + nums[j]) % basket
                    break

        return dp[-1] == 0


# 3rd solution
# O(k^n) time | O(k^n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort(reverse=True)
        target = total // k
        if nums[0] > target:
            return False

        @cache
        def dfs(i, mask, val):
            if i == k:
                return True

            for idx in range(n):
                if (mask >> idx) & 1:
                    continue
                new = val + nums[idx]
                newMask = mask | (1 << idx)
                if new > target:
                    continue
                elif new < target:
                    if dfs(i, newMask, new):
                        return True
                else:
                    if dfs(i + 1, newMask, 0):
                        return True
            return False

        return dfs(0, 0, 0)


# 4th solution
# O(k^n) time | O(k + n) space
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        target = sum_nums // k
        nums = sorted(nums, reverse=True)  # 先用最大的值填充，减小回溯次数
        if nums[0] > target:
            return False

        bucket = [0] * k  # 存储的是每个桶中的总和

        # 球选桶的视角进行，回溯方法判断当前球放入第i个桶的时候是否合适，当最终桶中元素不符合要求，进行回溯
        def backtrack(idx):
            if idx == len(nums):  # 此处需要使用len(nums)如果减1最后一个元素不能加上去
                return True
            # 否则开始判断填到哪个桶中
            for i in range(k):
                # 如果当前桶和上一个桶总和相同，加入新元素结果也必然相同，因此跳过
                if i > 0 and bucket[i] == bucket[i - 1]:
                    continue
                if bucket[i] + nums[idx] > target:
                    continue  # 超出就不加
                # 否则就加入
                bucket[i] += nums[idx]
                # 回溯下一个元素
                if backtrack(idx + 1):
                    return True
                # 最终结果不满足就回溯
                bucket[i] -= nums[idx]
            return False

        return backtrack(0)