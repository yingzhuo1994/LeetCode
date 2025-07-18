# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        min_h = nums[-n:]
        heapify(min_h)

        suf_max = [0] * (m - n + 1)  # 后缀最大和
        suf_max[-1] = sum(min_h)
        for i in range(m - n - 1, n - 1, -1):
            suf_max[i] = suf_max[i + 1] + nums[i] - heappushpop(min_h, nums[i])

        max_h = [-x for x in nums[:n]]  # 所有元素取反，表示最大堆
        heapify(max_h)

        pre_min = -sum(max_h)  # 前缀最小和
        ans = pre_min - suf_max[n]  # i=n-1 时的答案
        for i in range(n, m - n):
            pre_min += nums[i] + heappushpop(max_h, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])
        return ans