# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        while seats[i] != 1:
            i += 1
        ans = i
        last = i
        while i < len(seats) - 1:
            if seats[i] == 1:
                ans = max(ans, (i - last) // 2)
                last = i
            i += 1
        ans = max(ans, (i - last) // 2)
        if seats[i] == 0:
            ans = max(ans, i - last)        
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                ans = max(ans, i if last < 0 else (i - last) // 2)
                last = i
        return max(ans, n - last - 1)