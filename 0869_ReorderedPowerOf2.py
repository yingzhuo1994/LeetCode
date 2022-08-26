# 1st solution
# O(k!) time | O(k) space
# where k is the length of n
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = []
        while n > 0:
            d = n % 10
            nums.append(d)
            n //= 10
        nums.sort()
        firstIdx = bisect.bisect_left(nums, 1)

        visited = [False] * len(nums)
        def dfs(length, num):
            if length == len(nums):
                if 2**32 % num == 0:
                    return True
                return False
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if dfs(length + 1, num * 10 + nums[i]):
                        return True
                    visited[i] = False
            return False
        
        for i in range(firstIdx, len(nums)):
            visited[i] = True
            if dfs(1, nums[i]):
                return True
            visited[i] = False
        
        return False

# 2nd solution
# O((log(n))^2) time | O(log(n)) space
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << d)) for d in range(31))