class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1st solution
        # O(nlogn) time | O(1) space
        nums.sort()
        return nums[-k]
    
        # 2nd solution, bubble sort idea
        # O(nk) time | O(1) space
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    # exchange elements, time consuming
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[-k]
    
        # 3rd solution, selection sort idea
        # O(nk) time | o(1) space
        for i in range(len(nums), len(nums)-k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[-k]