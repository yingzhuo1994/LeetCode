# 1st solution
# O(n) time | O(n) space
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for num in cnt:
            if num == cnt[num]:
                ans = max(ans, num)
        return ans