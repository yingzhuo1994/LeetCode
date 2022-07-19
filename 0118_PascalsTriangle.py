# 1st Recursive Solution
# O(n^2) time | O(n^2) space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        ans = self.generate(numRows - 1)
        lst = [1 for _ in range(numRows)]
        lastRow = ans[-1]
        for i in range(1, numRows - 1):
            lst[i] = lastRow[i - 1] + lastRow[i]
        ans.append(lst)
        return ans

# 2nd Iterative Solution
# O(n^2) time | O(n^2) space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        for i in range(2, numRows + 1):
            curRow = [1 for _ in range(i)]
            lastRow = lst[-1]
            for j in range(1, i - 1):
                curRow[j] = lastRow[j - 1] + lastRow[j]
            lst.append(curRow)
        return lst

# 3rd Solution
# O(n^2) time | O(n^2) space
class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res
