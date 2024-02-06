# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        ans = 0
        hp = 1
        minHeap = []
        for x in nums:
            if x < 0:
                heappush(minHeap, x)
            hp += x
            if hp < 1:
                # 这意味着 x < 0，所以前面必然会把 x 入堆
                # 所以堆必然不是空的，并且堆顶 <= x
                hp -= heappop(minHeap)  # 反悔
                ans += 1
        return ans