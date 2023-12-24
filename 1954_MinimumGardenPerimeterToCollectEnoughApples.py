# 1st solution
# O(m^(1/3)) time | O(1) space
# m = neededApples
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0
        s = 0
        while s < neededApples:
            n += 1
            s += 12 * n**2
        return 8 * n

# 2nd solution
# O(log(m)) time | O(1) space
# m = neededApples
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right, ans = 1, 100000, 0
        while left <= right:
            mid = (left + right) // 2
            s = 2 * mid * (mid + 1) * (mid * 2 + 1)
            if s >= neededApples:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans * 8