class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1st solution
        # O(nlogn) time | O(1) space
        nums.sort()
        return nums[-k]