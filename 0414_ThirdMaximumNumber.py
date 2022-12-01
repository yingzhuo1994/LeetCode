class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num in (a, b, c):
                continue
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
        if c == float("-inf"):
            return a
        return c