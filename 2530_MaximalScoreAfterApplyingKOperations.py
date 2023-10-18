# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = [-num for num in nums]
        heapify(hp)
        ans = 0
        for _ in range(k):
            num = -heappop(hp)
            ans += num
            num = ceil(num / 3)
            heappush(hp, -num)
        
        return ans