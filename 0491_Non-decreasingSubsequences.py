# 1st solution
# O(n^2 *2^n) time | O(n^2 *2^n) space
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arrays = [[] for _ in nums]
        visited = set()
        for i in range(1, len(nums)):
            for j in reversed(range(i)):
                if nums[j] <= nums[i]:
                    for lst in arrays[j]:
                        arrays[i].append(lst + [nums[i]])
                    if (nums[j], nums[i]) not in visited:
                        arrays[i].append([nums[j], nums[i]])
                        visited.add((nums[j], nums[i]))
                    if nums[j] == nums[i]:
                        break
        ans = []
        for array in arrays:
            ans.extend(array)
        return ans


