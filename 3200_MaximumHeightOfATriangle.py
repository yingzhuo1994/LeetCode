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


# 2nd solution
# O(1) time | O(1) space
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def helper(first, second):
            a = math.floor(math.sqrt(first))
            b = math.floor((math.sqrt(1 + 4 * second) - 1) / 2)
            if a > b:
                return 2 * b + 1
            else:
                return 2 * a
        
        ans = max(helper(red, blue), helper(blue, red))
        return ans