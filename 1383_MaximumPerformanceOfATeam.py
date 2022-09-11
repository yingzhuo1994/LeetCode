# 1st solution
# O(n*log(n)) time | O(n + k) space
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7

        engineers = [[ef, sd] for ef, sd in zip(efficiency, speed)]
        engineers.sort(reverse=True)

        sumSpeed, ans, heap = 0, 0, []
        
        for eff, speed in engineers:
            if len(heap) > k - 1: sumSpeed -= heappop(heap)
            heappush(heap, speed)
            sumSpeed += speed
            ans = max(ans, sumSpeed*eff)
        
        return ans % MOD
