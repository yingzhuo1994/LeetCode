# 1st solution
# O(n) time | O(1) space
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        last = -1
        ans = 0
        count = 0
        for i in range(n):
            if forts[i] == 0:
                count += 1
                continue
            
            if last >= 0 and forts[i] * forts[last] == -1:
                ans = max(ans, count)
            
            count = 0
            last = i
        
        return ans
