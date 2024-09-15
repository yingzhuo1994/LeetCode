# 1st solution
# O(kn) time | O(n) space
# where k = len(nums), n = 100
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [False] * 100
        for a, b in nums:
            points[a:b+1] = [True] * (b - a + 1)
        return sum(points)


# 2nd solution
# O(k * log(k)) time | O(k) space
# where k = len(nums)
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda v: [v[0], -v[1]])
        stack = []
        for a, b in nums:
            if not stack or stack[-1][1] < a:
                stack.append([a, b])
            else:
                stack[-1][1] = max(stack[-1][1], b)
        ans = 0
        for a, b in stack:
            ans += b - a + 1
        return ans