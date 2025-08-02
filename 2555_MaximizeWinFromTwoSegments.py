# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        ans = mx = left = right = 0
        for mid, p in enumerate(prizePositions):
            # 把 prizePositions[mid] 视作第二条线段的左端点，计算第二条线段可以覆盖的最大奖品下标
            while right < n and prizePositions[right] - p <= k:
                right += 1
            # 循环结束后，right-1 是第二条线段可以覆盖的最大奖品下标
            ans = max(ans, mx + right - mid)
            # 把 prizePositions[mid] 视作第一条线段的右端点，计算第一条线段可以覆盖的最小奖品下标
            while p - prizePositions[left] > k:
                left += 1
            # 循环结束后，left 是第一条线段可以覆盖的最小奖品下标
            mx = max(mx, mid - left + 1)
        return ans