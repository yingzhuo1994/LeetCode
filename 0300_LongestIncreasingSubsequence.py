class Solution:
    # 1st solution
    # O(n^2) time | O(n) space
    def lengthOfLIS(self, nums: List[int]) -> int:
        countLst = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    countLst[i] = max(countLst[j] + 1, countLst[i])
        return max(countLst)

        