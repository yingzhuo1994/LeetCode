# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        first = colors[-2]
        second = colors[-1]
        ans = 0
        for color in colors:
            if first != second and second != color:
                ans += 1
            first, second = second, color
        return ans