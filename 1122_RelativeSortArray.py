# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idxDic = {num: i for i, num in enumerate(arr2)}
        n = len(arr1)
        arr1.sort(key=lambda v: idxDic.get(v, v + n))
        return arr1

