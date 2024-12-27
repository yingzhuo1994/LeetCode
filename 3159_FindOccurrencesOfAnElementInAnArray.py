# 1st solution
# O(n) time | O(n) space
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        lst = []
        for i, num in enumerate(nums):
            if num == x:
                lst.append(i)
        return [lst[i - 1] if i <= len(lst) else -1 for i in queries]