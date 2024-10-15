# 1st solution
# O(log(a + b)) time | O(1) space
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def helper(first, second):
            a = b = 0
            k = 1
            layer = 1
            while True:
                if layer == 1:
                    a += k
                else:
                    b += k
                if a > first or b > second:
                    break
                layer *= -1
                k += 1
            return k - 1
        ans = max(helper(red, blue), helper(blue, red))
        return ans
