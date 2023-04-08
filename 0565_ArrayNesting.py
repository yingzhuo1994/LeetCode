# 1st solution
# O(n) time | O(n) space
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(idx, visited, depth=0):
            if idx in visited:
                return depth
            visited.add(idx)
            return dfs(nums[idx], visited, depth + 1)
        ans = 0
        visited = set()
        for i in range(len(nums)):
            length = dfs(i, visited)
            ans = max(ans, length)
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(idx, depth=0):
            idx %= n
            if nums[idx] >= n:
                return depth
            nums[idx] += n
            return dfs(nums[idx], depth + 1)
        ans = 0
        for i in range(len(nums)):
            length = dfs(i)
            ans = max(ans, length)
        return ans

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(len(nums)):
            idx = i
            length = 0
            while nums[idx] < n:
                nums[idx] += n
                idx = nums[idx] % n
                length += 1
            ans = max(ans, length)

        return ans