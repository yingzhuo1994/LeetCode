# 1st solution
# O(m * n * log(n)) time | O(m + n) space
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def query(i, j):
            array = nums[i:j+1]
            array.sort()
            diff = array[1] - array[0]
            return all(array[i+1] - array[i] == diff for i in range(len(array) - 1))
        
        return [query(i, j) for i, j in zip(l, r)]