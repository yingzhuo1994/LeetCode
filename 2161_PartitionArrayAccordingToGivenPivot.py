# 1st solution
# O(n) time | O(n) space
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        front = []
        middle = []
        back = []
        for num in nums:
            if num < pivot:
                front.append(num)
            elif num > pivot:
                back.append(num)
            else:
                middle.append(num)
        ans = front + middle + back
        return ans