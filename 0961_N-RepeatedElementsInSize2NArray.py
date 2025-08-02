# 1st solution
# O(n) time | O(n) space
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = None
        freq = 0
        for num in cnt:
            if cnt[num] > freq:
                freq = cnt[num]
                ans = num
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] or nums[i] == nums[i - 2]:
                return nums[i]
        return nums[0]