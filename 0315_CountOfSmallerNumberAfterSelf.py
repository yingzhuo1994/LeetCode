class Solution:
    # 1st solution
    # O(n^2) time | O(n) space
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in nums]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    counts[i] += 1
        return counts