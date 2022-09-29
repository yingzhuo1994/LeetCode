# 1st solution
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[-k:]
        if abs(arr[idx - 1] - x) <= abs(arr[idx] - x):
            idx -= 1
        left, right = idx - 1, idx + 1
        ans = [arr[idx]]
        while left >= 0 and right < len(arr) and len(ans) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        ans.sort()
        diff = k - len(ans)
        if diff == 0:
            return ans
        if left < 0:
            return ans + arr[right:right+diff]
        else:
            return arr[left+1-diff:left+1] + ans
