# 1st solution
# O(n * sqrt(U/k) + m) time | O(U/k) space
# where n = len(nums1), m = len(nums2), U = max(nums1)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = defaultdict(int)
        for x in nums1:
            if x % k:
                continue
            x //= k
            for d in range(1, isqrt(x) + 1):  # 枚举因子
                if x % d:
                    continue
                cnt[d] += 1  # 统计因子
                if d * d < x:
                    cnt[x // d] += 1  # 因子总是成对出现
        return sum(cnt[x] for x in nums2)