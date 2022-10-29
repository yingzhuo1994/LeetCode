# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = [[t1, t2] for t1, t2 in zip(plantTime, growTime)]
        time = 0
        ans = 0
        plants.sort(key = lambda v: [-v[1], v[0]])
        for t1, t2 in plants:
            ans = max(ans, time + t1 + t2)
            time += t1
        return ans + 1
