# 1st solution
# O(n * log(n) + n * log(k)) time | O(n) space
# where n = len(position), k = max(position)
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def enough(target):
            count = 1
            dist = 0
            for i in range(1, len(position)):
                dist += position[i] - position[i-1]
                if dist >= target:
                    dist = 0
                    count += 1
            return count >= m

        position.sort()
        start = 1
        end = max(position)
        ans = 1
        while start <= end:
            mid = start + (end - start) // 2
            if enough(mid):
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans