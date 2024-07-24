# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform(num):
            s = str(num)
            lst =[str(mapping[int(ch)]) for ch in s]
            value = int("".join(lst))
            return value
        ans = sorted(nums, key=lambda num: transform(num))
        return ans