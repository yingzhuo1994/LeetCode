# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in nums]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    counts[i] += 1
        return counts

# 2nd solution
# O(nlogn) time | O(n) space
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(enum):
            half = len(enum) // 2
            if half:
                left, right = mergeSort(enum[:half]), mergeSort(enum[half:])
                for i in reversed(range(len(enum))):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        mergeSort(list(enumerate(nums)))
        return smaller