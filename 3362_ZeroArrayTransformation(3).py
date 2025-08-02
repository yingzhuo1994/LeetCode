# 1st solution
# O(n + q * log(q)) time | O(n + q) space
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda q: q[0])  # 按照左端点从小到大排序
        h = []
        diff = [0] * (len(nums) + 1)
        sum_d = j = 0
        for i, x in enumerate(nums):
            sum_d += diff[i]
            # 维护左端点 <= i 的区间
            while j < len(queries) and queries[j][0] <= i:
                heappush(h, -queries[j][1])  # 取相反数表示最大堆
                j += 1
            # 选择右端点最大的区间
            while sum_d < x and h and -h[0] >= i:
                sum_d += 1
                diff[-heappop(h) + 1] -= 1
            if sum_d < x:
                return -1
        return len(h)