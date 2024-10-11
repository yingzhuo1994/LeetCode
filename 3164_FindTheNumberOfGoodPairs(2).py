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


# 2nd solution
# O(n + m +  (U/k) * log(m)) time | O(n + m) space
# where n = len(nums1), m = len(nums2), U = max(nums1)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt1 = Counter(x // k for x in nums1 if x % k == 0)
        if not cnt1:
            return 0

        ans = 0
        u = max(cnt1)
        cnt2 = Counter(nums2)
        for x, cnt in cnt2.items():
            s = sum(cnt1[y] for y in range(x, u + 1, x))  # 枚举 x 的倍数
            ans += s * cnt
        return ans