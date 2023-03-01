# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(array):
            if len(array) <= 1:
                return array
            n = len(array)
            mid = n // 2
            left = mergesort(array[:mid])
            right = mergesort(array[mid:])
            ans = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            ans.extend(left[i:] or right[j:])
            return ans

        return mergesort(nums)