# 1st solution
# O(mn * log(mn)) time | O(mn) space
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array = []
        for row in grid:
            array.extend(row)
            r = array[0] % x
            for num in row:
                if num % x != r:
                    return -1
        
        array.sort()

        total = 0
        target = array[0]
        for i in reversed(range(len(array))):
            total += array[i] - target

        ans = total
        for i in range(1, len(array)):
            diff = array[i] - array[i - 1]
            total += (2 * i - len(array)) * diff
            ans = min(ans, total)
        return ans // x