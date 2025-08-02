# 1st solution
# O(n) time | O(k) space
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        que = collections.deque()
        res = 0
        for i in range(n):
            if que and i >= que[0] + k:
                que.popleft()
            if len(que) % 2 == nums[i]:
                if i +  k > n: return -1
                que.append(i)
                res += 1
        return res