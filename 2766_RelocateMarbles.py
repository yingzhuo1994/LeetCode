# 1st solution, MLE
# O(M) time | O(M) space
# where M is the largest location
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        n = max(max(nums), max(moveTo)) + 1
        locations = [0] * n
        for num in nums:
            locations[num] = 1
        for a, b in zip(moveFrom, moveTo):
            locations[a] = 0
            locations[b] = 1
        ans = [i for i in range(n) if locations[i] > 0]
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        locations = {}
        for num in nums:
            locations[num] = 1
        for a, b in zip(moveFrom, moveTo):
            del locations[a]
            locations[b] = 1
        return sorted(list(locations.keys()))