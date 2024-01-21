# 1st solution, MLE
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        array = [abs(nums[i] - nums[j]) for i in range(n) for j in range(i)]
        array.sort()
        return array[k - 1]

