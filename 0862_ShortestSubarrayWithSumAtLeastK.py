# 1st solution
# O(n) time | O(n) space
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = len(nums) + 1
        s = list(accumulate(nums, initial=0))  # 计算前缀和
        q = deque()
        for i, cur_s in enumerate(s):
            while q and cur_s - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())  # 优化一
            while q and s[q[-1]] >= cur_s:
                q.pop()  # 优化二
            q.append(i)
        return ans if ans <= len(nums) else -1